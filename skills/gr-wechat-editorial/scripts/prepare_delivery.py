#!/usr/bin/env python3
"""Build a fresh local review package. No network or credential access."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ALLOWED = {'title', 'author', 'digest', 'content', 'content_source_url', 'thumb_media_id'}

class CheckHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'iframe', 'object', 'embed', 'form', 'style', 'link', 'base'}:
            self.errors.append('unsupported active or external-style element')
        for key, value in attrs:
            value = value or ''
            if key.lower().startswith('on'):
                self.errors.append('event handler not allowed')
            if key in {'src', 'href'} and value and not value.lower().startswith(('https://', 'http://', '#')):
                self.errors.append('unresolved local asset or unsupported link scheme')
            if key == 'style' and re.search(r'url\s*\(|expression\s*\(|@import', value, re.I):
                self.errors.append('external or active CSS not supported')
    handle_startendtag = handle_starttag

def prepare(data):
    if not isinstance(data, dict) or set(data) - ALLOWED:
        raise ValueError('expected article object with documented fields only')
    if not all(isinstance(v, str) for v in data.values()):
        raise ValueError('article values must be strings')
    if not data.get('title', '').strip() or not data.get('content', '').strip():
        raise ValueError('title and content required')
    result = dict(data)
    result['content'] = re.sub(r'<!--[\s\S]*?-->', '', result['content'])
    if '<!--' in result['content']:
        raise ValueError('unclosed internal comment')
    if re.search(r'placeholder|\{embed:|\bTODO\b', result['content'], re.I):
        raise ValueError('unresolved placeholder')
    parser = CheckHTML(); parser.feed(result['content']); parser.close()
    if parser.errors:
        raise ValueError('; '.join(sorted(set(parser.errors))))
    return result

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--article', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    try:
        data = prepare(json.loads(args.article.read_text(encoding='utf-8')))
        encoded = (json.dumps(data, ensure_ascii=False, indent=2)+'\n').encode('utf-8')
        args.out.mkdir(parents=True, exist_ok=False)
        (args.out/'article.json').write_bytes(encoded)
        (args.out/'article.html').write_text(data['content'], encoding='utf-8')
        manifest = {'status':'local_prepared', 'uploaded':False, 'published':False,
                    'article_sha256':hashlib.sha256(encoded).hexdigest(),
                    'cover_media_present':bool(data.get('thumb_media_id')),
                    'review':'Source, rights, mobile appearance and account readback require separate checks.'}
        (args.out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
        print('Local package prepared; not uploaded or published.')
    except (ValueError, OSError) as exc:
        ap.exit(1, f'Cannot prepare package: {exc}\n')

if __name__ == '__main__':
    main()
