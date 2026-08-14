#!/usr/bin/env ruby
# frozen_string_literal: true

# Zero-dependency release gate for every distributable Gingiris skill.
require "json"
require "yaml"
require "pathname"

ROOT = Pathname.new(__dir__).parent
SKILLS = ROOT.join("skills")
BANNED = [
  %r{github\.com/Gingiris/}, %r{gingiris\.github\.io},
  %r{clawhub\.ai/(?:user/)?gingiris/}i,
  %r{https?://gingiris\.com(?:/|\b)}
].freeze
PRIVATE_PATHS = {
  "gingiris-twitter-agent-ops" => ["references/weiyipei-ops.md"],
  "gr-backlinks" => ["data"]
}.freeze

errors = []
warnings = []
rows = []

SKILLS.children.select(&:directory?).sort.each do |dir|
  slug = dir.basename.to_s
  skill_file = dir.join("SKILL.md")
  unless skill_file.file?
    errors << "#{slug}: missing SKILL.md"
    next
  end
  text = skill_file.read
  match = text.match(/\A---\n(.*?)\n---\n/m)
  unless match
    errors << "#{slug}: invalid or missing YAML frontmatter"
    next
  end
  begin
    meta = YAML.safe_load(match[1], permitted_classes: [], aliases: false)
  rescue StandardError => e
    errors << "#{slug}: YAML parse failed: #{e.message}"
    next
  end
  name = meta.is_a?(Hash) ? meta["name"].to_s : ""
  description = meta.is_a?(Hash) ? meta["description"].to_s.strip : ""
  errors << "#{slug}: name is #{name.inspect}, expected #{slug.inspect}" unless name == slug
  errors << "#{slug}: description is empty" if description.empty?
  warnings << "#{slug}: description has no explicit trigger language" unless description.match?(/trigger|use this skill|when you need|适用|触发/i)

  public_files = dir.glob("**/*").select(&:file?).reject do |path|
    relative = path.relative_path_from(dir).to_s
    relative.start_with?("#{slug}/") || PRIVATE_PATHS.fetch(slug, []).any? do |private_path|
      relative == private_path || relative.start_with?("#{private_path}/")
    end
  end
  public_files.each do |path|
    next unless %w[.md .json .yaml .yml .txt .html].include?(path.extname)
    body = path.read
    BANNED.each do |pattern|
      errors << "#{path.relative_path_from(ROOT)}: banned public reference #{pattern.inspect}" if body.match?(pattern)
    end
  end

  nested = dir.join(slug)
  if nested.directory?
    public_files.each do |source|
      relative = source.relative_path_from(dir)
      target = nested.join(relative)
      errors << "#{slug}: nested package missing #{relative}" unless target.file?
      errors << "#{slug}: nested package differs at #{relative}" if target.file? && source.binread != target.binread
    end
    PRIVATE_PATHS.fetch(slug, []).each do |private_path|
      errors << "#{slug}: private path leaked into nested package: #{private_path}" if nested.join(private_path).exist?
    end
  end
  body = text.sub(match[0], "")
  rows << {
    slug: slug, bytes: text.bytesize,
    references: public_files.count { |path| path.to_s.include?("/references/") },
    scripts: public_files.count { |path| path.to_s.include?("/scripts/") },
    nested: nested.directory?,
    execution_sections: body.scan(/^##+\s+.*(?:执行|execution|workflow|SOP|output|输出|步骤|step)/i).length
  }
end

expected = SKILLS.children.count(&:directory?)
errors << "inventory mismatch: found #{rows.length} valid skills out of #{expected}" unless rows.length == expected
summary = {
  generated_at: Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ"), skills_checked: expected,
  passed: errors.empty?, error_count: errors.length, warning_count: warnings.length,
  with_nested_packages: rows.count { |row| row[:nested] },
  with_scripts: rows.count { |row| row[:scripts].positive? }, skills: rows
}
puts JSON.pretty_generate(summary.reject { |key, _| key == :skills })
warnings.each { |warning| warn "WARN: #{warning}" }
errors.each { |error| warn "ERROR: #{error}" }
report_path = ENV["GINGIRIS_SKILL_REPORT"]
File.write(report_path, JSON.pretty_generate(summary) + "\n") if report_path && !report_path.empty?
exit(errors.empty? ? 0 : 1)
