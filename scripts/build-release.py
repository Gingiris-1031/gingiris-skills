#!/usr/bin/env python3
"""Build inspectable public skill packages without runtime/private files. No upload."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'.md', '.py', '.sh', '.rb', '.json', '.yaml', '.yml', '.toml', '.txt', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.csv'}
PRIVATE = {'gr-backlinks': ('data/',), 'gingiris-twitter-agent-ops': ('references/weiyipei-ops.md',)}

def distributable(skill, relative):
    parts = relative.parts
    text = relative.as_posix()
    if any(p.startswith('.') or p in {'__pycache__', 'node_modules', 'data', 'logs'} for p in parts):
        return False
    if parts[0] == skill or (skill == 'gr-core' and parts[0] == 'gr'):
        return False
    if any(text == x.rstrip('/') or text.startswith(x) for x in PRIVATE.get(skill, ())):
        return False
    return relative.suffix.lower() in ALLOWED or relative.name in {'LICENSE', 'NOTICE'}

def build(output):
    output = output.resolve()
    if output.exists():
        raise ValueError('Choose a new output directory; existing artifacts are never overwritten')
    output.mkdir(parents=True)
    manifest = []
    for src in sorted((ROOT / 'skills').iterdir()):
        if not (src / 'SKILL.md').is_file():
            continue
        for file in sorted(src.rglob('*')):
            rel = file.relative_to(src)
            if file.is_symlink():
                raise ValueError(f'Symlink requires manual review: {file}')
            if not file.is_file() or not distributable(src.name, rel):
                continue
            target = output / src.name / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, target)
            manifest.append({'path': str(target.relative_to(output)), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    print(f'{len(build(args.output))} public files staged; no upload performed')
