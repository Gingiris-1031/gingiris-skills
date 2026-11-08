# Use Gingiris Skills with OpenClaw

These are task instructions, not a gateway plugin. You can install a complete package from a local Git checkout without a ClawHub account.

## Install one workflow

```bash
git clone https://github.com/Gingiris-1031/gingiris-skills.git
openclaw skills install ./gingiris-skills/skills/gr-social-distill --global
openclaw skills info gr-social-distill --json
```

Use a new checkout directory if that name already exists. Do not overwrite an existing installation without reviewing its local changes. Replace `gr-social-distill` with the exact desired package directory. Omit `--global` to use the active agent workspace instead of the shared managed directory.

## Verified installation scope

Checked with OpenClaw 2026.11.2 on 2026-11-08 in an isolated state directory:

- `gingiris-seo-geo`
- `competitor-research-playbook`
- `gingiris-user-interview`
- `gr-social-distill`

The installation check compares every packaged file with its installed copy and requires `eligible: true` and `modelVisible: true` in `skills info`. This verifies package installation and discovery, not completion of a growth task or a live model call. Other packages have not been individually tested in OpenClaw.

If the CLI says files were installed but Gateway refresh failed, an authenticated running Gateway has not reloaded them. Reconnect or restart your own Gateway normally; do not disable authentication to suppress the message. Start a fresh agent session after installation.

## First task

For `gr-social-distill`, supply an article and ask: “Create one LinkedIn draft from this source, preserve attribution, identify unsupported claims, and do not publish.” For research workflows, provide the product, target market, decision and available evidence. API credentials or external integrations required by a task are separate from skill installation.

完整目录及引用文件必须一起安装。`eligible` 表示加载条件满足，不表示任务结果已经验证；对外发布、联系他人和付费操作仍应遵循用户授权。

[Workflow directory](https://tools.gingiris.com/skills/) · [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)
