#!/usr/bin/env python3
"""Generate standalone competitor aliases; --check detects maintenance drift."""
import argparse
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--check', action='store_true')
a = p.parse_args()
src = ROOT/'skills/competitor-research-playbook'
text = (src/'SKILL.md').read_text()
outputs = {}
for f in src.rglob('*'):
    if f.is_file() and '__pycache__' not in f.parts:
        rel = f.relative_to(src)
        data = f.read_bytes()
        if str(rel) == 'SKILL.md':
            data = text.replace('name: competitor-research-playbook\n','name: gr-competitor-research\n',1).encode()
        outputs[ROOT/'skills/gr-competitor-research'/rel] = data
outputs[ROOT/'skills/gr-competitor/references/research-workflow.md'] = text.split('---',2)[2].lstrip().replace('(references/','(research/').encode()
for f in (src/'references').rglob('*'):
    if f.is_file():
        data = f.read_bytes()
        if f.name == 'README.md':
            data = data.replace(b'../../SKILL.md', b'../../research-workflow.md')
        outputs[ROOT/'skills/gr-competitor/references/research'/f.relative_to(src/'references')] = data
bad=[]
for path,data in outputs.items():
    if not path.exists() or path.read_bytes()!=data:
        bad.append(str(path.relative_to(ROOT)))
        if not a.check:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
if a.check and bad:
    print('Drift:\n'+'\n'.join(bad));sys.exit(1)
print(f'{"Checked" if a.check else "Synchronized"} {len(outputs)} generated files')
