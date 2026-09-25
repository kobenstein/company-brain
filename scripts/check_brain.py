#!/usr/bin/env python3
"""Read-only, local structural checks for this Markdown Company Brain.

No network, installs, account access, or modifications. Does not establish
historical completeness, legal accuracy, or validity of business hypotheses.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_STATUS = {'CORE','DECISION','HYPOTHESIS','RESEARCH','LEARNING','OPEN','ARCHIVED','DRAFT','SYNTHESIS','CURRENT'}
KNOWN_SOURCES = {f'S{i:02d}' for i in range(1,13)} | {f'W{i:02d}' for i in range(1,12)}

def check() -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    ids: set[str] = set()
    checked_links = 0
    files = sorted(ROOT.rglob('*.md'))
    files = [p for p in files if '.git' not in p.parts]
    for p in files:
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            errors.append(f'{rel}: frontmatter missing')
            continue
        fm = text.split('---\n',2)[1]
        fields = {}
        for line in fm.splitlines():
            if ':' in line:
                key,val = line.split(':',1)
                fields[key]=val.strip()
        for key in ('id','title','status','authority','reviewed_on','source_ids','sensitivity'):
            if not fields.get(key): errors.append(f'{rel}: missing {key}')
        sid = fields.get('id')
        if sid in ids: errors.append(f'{rel}: duplicate id {sid}')
        if sid: ids.add(sid)
        if fields.get('status') not in ALLOWED_STATUS: errors.append(f'{rel}: unknown status')
        try:
            src = json.loads(fields.get('source_ids','[]'))
            if not src or not set(src).issubset(KNOWN_SOURCES): errors.append(f'{rel}: invalid source_ids')
        except (ValueError,TypeError): errors.append(f'{rel}: source_ids not valid JSON list')
        # Strip fenced code so illustrative paths are not treated as actual links.
        body = re.sub(r'```.*?```','',text,flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^\s]+?)(?:\s+"[^"]*")?\)',body):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'): continue
            target = unquote(link.split('#',1)[0])
            if not target: continue
            checked_links += 1
            resolved = (p.parent/target).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f'{rel}: link escapes repo: {target}')
            elif not resolved.exists():
                msg=f'{rel}: missing local link {target}'
                (warnings if 'research/archive/' in rel else errors).append(msg)
        for pat in (r'\bsk-[A-Za-z0-9]{20,}',r'\bgh[pousr]_[A-Za-z0-9]{20,}',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'):
            if re.search(pat,text): errors.append(f'{rel}: possible credential, inspect before sharing')
    return {'markdown_files':len(files),'local_links_checked':checked_links,'errors':errors,'warnings':warnings,
            'limitations':'Structural checks only. No external-link validation, exhaustive secrets audit, or complete chat-history verification.'}

if __name__=='__main__':
    result=check()
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(1 if result['errors'] else 0)
