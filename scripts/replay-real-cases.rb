#!/usr/bin/env ruby
# frozen_string_literal: true

# Historical real-case replay for the 41 skills listed on gingiris.tools/skills.
# This is a backtest of decision coverage, not a claim that rerunning a prompt
# caused the historical business outcome.

require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent
CASE_ROOT = ROOT.parent.join("growth-tools", "cases")

CASES = {
  "launch" => ["launch-cac-6-dollars", "~500K visits, ~800 signups, CAC $6.25", [/UTM|attribution/i, /channel|渠道/i, /CAC|conversion|转化/i]],
  "ph" => ["vote-pacing-lesson", "Historical support was reviewed in two-hour windows", [/100.{0,12}(upvotes|votes|票).{0,12}(hour|小时)/i, /two.hour|two hour|2.{0,3}(hour|小时)/i, /buy|vote exchange|购买|换票/i]],
  "small_launch" => ["1k-launch-recipe", "$1K produced a few hundred signups", [/\$?1.?000|\$1K|千元/i, /Reddit|subreddit/i, /YouTube/i]],
  "kol_launch" => ["15k-budget-4m-impressions", "$15K, 35 creators, 4M impressions, ~10K signups", [/KOL|creator|influencer|红人/i, /burst|集中|协同|24.{0,3}48/i, /conversion|注册|转化/i]],
  "oss" => ["open-source-60k-stars-origin", "AFFiNE: 0→60K stars in 24 months", [/README/i, /community|社区/i, /interview|访谈|user/i]],
  "oss_launch" => ["music-model-6k-stars-week1", "Open-source music model: ~6K stars in week one", [/Reddit/i, /Hacker News|\bHN\b/i, /competitor|window|竞品|窗口/i]],
  "oss_b2b" => ["apache-project-campaign", "Apache ecosystem project: 200K impressions and +401 stars in 10 days", [/README/i, /comparison|对比/i, /backlink|sponsor|反链/i]],
  "readme" => ["open-source-60k-stars-origin", "AFFiNE README was the highest-viewed conversion surface", [/tagline/i, /quick start/i, /demo|hero/i]],
  "twitter" => ["quote-stacking-700k", "Owned-account operations must route multi-creator campaigns", [/MASTER-STATUS/i, /source.index|素材库/i, /KOL|creator|launch/i]],
  "consulting" => ["b2b-0-to-500k-arr", "Consulting must diagnose stage before prescribing channels", [/stage|阶段/i, /activation|激活/i, /two.week|two week|2周|两周/i]],
  "seed_growth" => ["attribution-over-applause", "Growth must be stage-gated and cohort-attributed", [/first 10|first.ten|前10|前十/i, /activation|激活/i, /source.{0,8}signup.{0,8}activated/i]],
  "zero_budget" => ["1k-launch-recipe", "Zero-budget motion starts with targeted outreach and activation", [/200.{0,16}(outreach|message|私信|外联)/i, /Reddit/i, /activation|激活/i]],
  "viral" => ["anti-paid-growth-plan", "¥1M budget target: 500K registrations, implied CAC ¥2", [/CAC|获客成本/i, /referral|邀请|裂变/i, /UGC|ambassador|大使/i]],
  "agent_workflow" => ["agent-workflow-15-people-to-5-days", "15 people × 3–4 weeks reduced to one strategist + AI in 5 days", [/15.{0,12}(people|人).{0,16}3.{0,4}4.{0,8}(week|周)/i, /strategist|策略师/i, /harness|评测|evaluation/i]],
  "b2b" => ["b2b-0-to-500k-arr", "Founder-led B2B motion reached $500K ARR", [/founder|创始人/i, /PLG|SLG|sales/i, /ARR|revenue|收入/i]],
  "seo" => ["attribution-over-applause", "Channel attribution changed spend decisions", [/canonical|schema|结构化/i, /citation|GEO|引用/i, /measure|track|监控|日志/i]]
}.freeze

TESTS = {
  "gingiris-launch" => "launch", "product-hunt-playbook" => "ph",
  "product-hunt-launch-guide" => "ph", "startup-launch" => "small_launch",
  "startup-launch-playbook" => "small_launch", "ai-launch-playbook" => "kol_launch",
  "ai-product-launch" => "launch", "go-to-market-playbook" => "b2b",
  "gingiris-seo-geo-agent" => "seo", "gingiris-seo-geo" => "seo",
  "gingiris-b2b-growth" => "b2b", "saas-growth-playbook" => "b2b",
  "plg-playbook" => "b2b", "b2b-marketing-playbook" => "b2b",
  "saas-marketing-playbook" => "b2b", "gingiris-opensource" => "oss",
  "github-stars-playbook" => "oss_launch", "gingiris-github-star-growth" => "oss",
  "open-source-marketing-playbook" => "oss", "gr-readme" => "readme",
  "gingiris-aso-growth" => "small_launch", "aso-playbook" => "small_launch",
  "hardware-saas-gtm" => "kol_launch", "gingiris-kol-outreach" => "kol_launch",
  "kol-outreach" => "kol_launch", "gingiris-ugc-matrix" => "viral",
  "community-ambassador-playbook" => "viral", "community-building-playbook" => "oss",
  "devrel-playbook" => "oss_b2b", "developer-marketing-playbook" => "oss_b2b",
  "gingiris-reddit-marketing" => "oss_launch", "gingiris-twitter-agent-ops" => "twitter",
  "gingiris-user-interview" => "oss", "competitor-research-playbook" => "oss_launch",
  "startup-consultant" => "consulting", "startup-growth-playbook" => "seed_growth",
  "startup-marketing-playbook" => "zero_budget", "viral-marketing-playbook" => "viral",
  "growth-hacking-playbook" => "viral", "gingiris-growth-finder" => "b2b",
  "agent-workflow-playbook" => "agent_workflow"
}.freeze

def case_exists?(slug)
  CASE_ROOT.join(slug, "index.html").file?
end

rows = TESTS.map do |skill, case_key|
  case_slug, outcome, signals = CASES.fetch(case_key)
  path = ROOT.join("skills", skill, "SKILL.md")
  # Reddit is intentionally archived from the monorepo but remains on the
  # public catalog and local runtime; validate the installed source instead.
  path = Pathname.new(File.expand_path("~/.agents/skills/#{skill}/SKILL.md")) unless path.file?
  text = path.file? ? path.read : ""
  hits = signals.map { |signal| text.match?(signal) }
  coverage = hits.count(true).fdiv(signals.length)
  size_ok = text.bytesize >= 2_500
  status = if !case_exists?(case_slug) || text.empty?
             "FAIL"
           elsif coverage == 1.0 && size_ok
             "PASS"
           elsif coverage >= (2.0 / 3.0)
             "PARTIAL"
           else
             "FAIL"
           end
  {
    skill: skill, case: case_slug, known_outcome: outcome,
    signals_hit: hits.count(true), signals_total: signals.length,
    independent_depth: size_ok, status: status
  }
end

summary = {
  generated_at: Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
  method: "historical real-case decision-coverage backtest",
  disclaimer: "PASS means the skill independently covers the known winning/losing factors. It does not prove causal lift from a new campaign.",
  skills_tested: rows.length,
  pass: rows.count { |row| row[:status] == "PASS" },
  partial: rows.count { |row| row[:status] == "PARTIAL" },
  fail: rows.count { |row| row[:status] == "FAIL" },
  rows: rows
}

puts JSON.pretty_generate(summary)
report = ENV["GINGIRIS_REPLAY_REPORT"]
File.write(report, JSON.pretty_generate(summary) + "\n") if report && !report.empty?
exit(rows.any? { |row| row[:status] == "FAIL" } ? 1 : 0)
