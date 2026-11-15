# Fields and persistence / 字段与持久化

Keep three independent fields: evidence_status (verified / attributed / pending / unsupported), permission_status (allowed / unclear / restricted), delivery_status (source-needed / draft / review-needed / ready / authorized / submitted / scheduled / published-verified / measured; also blocked / failed / unknown / cancelled / draft-uploaded-verified). Verified evidence alone does not imply publication readiness. Properly attributed first-party material can be usable. Resolve material pending/unsupported claims by checking, qualifying or removing them; then reassess the draft. A published post can later need correction without erasing its delivery history.

For multi-session work, reuse the user's existing state store. Otherwise create a local task directory with README.md (scope, timezone, current version, next step), evidence.csv, calendar.csv and ledger.csv as needed. Record actual paths in the handoff. Store private raw material separately with limited access; never bundle it into a public skill. No new files are necessary for an ordinary single rewrite.

Ledger columns: operation_key, content_id, revision, platform, account, slot, timezone, authorization_scope, delivery_status, platform_id, verified_url, checked_at, owner, next_action. Key = content_id + platform + account + absolute slot. Revision is separate so editing copy does not bypass duplicate detection. A retry keeps the key. Rescheduling preserves the old row and requires applicable authorization. Check submitted/scheduled/published/unknown records before retry; the ledger is evidence of recorded work, not exhaustive platform history. Reconcile external changes when accessible.

Calendar fields: content_id, parent_id, date_time, timezone, platform, account, owner, reviewer, person_hours, evidence_link, asset_path, delivery_status, next_action. Capacity is summed person-hours, not elapsed time; show review and buffer separately. State an operational timezone, plus audience timezone when useful; handle daylight-saving conversion for dated slots.

Unassigned owner: unassigned(editor) plus assignment deadline. Untagged footage: to-be-tagged plus preparation task. Missing metrics: null/unknown plus reason, not zero. Missing permission: unclear plus scope/source to confirm, not an automatic conclusion based only on whether it was oral or written.

Platform-facts register (when a fact matters): platform | constraint | value | source/editor | checked_at | context | refresh_trigger. Recheck when stale, contradicted or editor behavior changes; do not require a fresh lookup of every stable fact every week.

中文对照：evidence_status=证据状态；permission_status=使用许可；delivery_status=交付状态；person_hours=人时；operation_key=操作键；verified_url=回读链接。Use the same field keys across exports; labels may be localized.
