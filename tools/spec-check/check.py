#!/usr/bin/env python3
"""Offline, deterministic checks for Stayora's Markdown specification."""
import argparse
import datetime as dt
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

RULES = {**{f'E{i}': 'ERROR' for i in range(1, 8)}, **{f'W{i}': 'WARN' for i in range(1, 5)}}
# These paths hold tooling and generated evidence, not specification documents.
# Only W1/W2 skip them; all ERROR rules still scan their Markdown files.
NON_SPEC_WARNING_PREFIXES = ('generated/', 'tools/', '.github/')
ADR = re.compile(r'\bADR-P\d{3}\b')
FD = re.compile(r'\bFD-\d{2}\b')
HEADING = re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$')
LINK = re.compile(r'(?<!!)\[[^]\n]+\]\((<[^>]+>|[^)]+)\)')
STATUSES = {'CONFIRMED', 'WORKING MODEL', 'HYPOTHESIS', 'TBD', 'OUT OF SCOPE — V0', 'SUPERSEDED', 'CONFIRMED — REFINED'}
DATE = re.compile(r'\b(20\d{2}-\d{2}-\d{2})\b')
SECRET = [re.compile(x) for x in (r'\b(?:sk-|xai-)[A-Za-z0-9_-]{12,}\b', r'\bgh[pousr]_[A-Za-z0-9]{20,}\b', r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', r'\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s/@:]+:[^\s/@]+@[^\s)]+', r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', r'(?<!\d)(?:\+84|0)(?:3|5|7|8|9)\d{8}(?!\d)', r'\bB\d{2}-\d{2}[A-Z]?\b')]
ENTROPY_TOKEN = re.compile(r'(?<![A-Za-z0-9])[A-Za-z0-9_+/=]{32,}(?![A-Za-z0-9])')
COUNT = re.compile(r'\b(\d+)\s*(?:ADRs?\b|(?:mục|items?)\s+(?:trong\s+)?contradiction[- ]audit\b|contradiction[- ]audit\s+(?:items?|mục)\b)', re.I)

def slug(s):
    s = re.sub(r'<[^>]+>', '', s).lower()
    s = re.sub(r'[^\w\- ]', '', s, flags=re.UNICODE).replace('_', '-')
    return re.sub(r'\s', '-', s).strip('-')

def clean(s):
    return re.sub(r'\*|`', '', s).strip().rstrip('.').strip()

def run(root, only=None, today=None, return_meta=False):
    root = Path(root).resolve()
    today = today or dt.date.today()
    docs = {p.relative_to(root).as_posix(): p.read_text(encoding='utf-8') for p in root.rglob('*.md') if '.git' not in p.parts}
    lines = {p: t.splitlines() for p, t in docs.items()}
    findings = []
    suppressed_w1_w2 = 0
    def add(rule, path, n, detail):
        if only and rule != only: return
        source = lines.get(path, [])
        excerpt = source[n-1].strip() if 0 < n <= len(source) else detail
        findings.append(dict(rule=rule, severity=RULES[rule], file=path, line=n, text=excerpt, detail=detail))
    decisions = '00-start-here/DECISIONS.md'
    founder = '11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md'
    adr_heads, adr_anchors, index, fd_rows = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    for n, line in enumerate(lines.get(decisions, []), 1):
        m = re.match(r'^### (ADR-P\d{3})\b', line)
        if m: adr_heads[m.group(1)].append(n)
        m = re.match(r'^<a id="(adr-p\d{3})"></a>\s*$', line)
        if m: adr_anchors[m.group(1).upper()].append(n)
        m = re.match(r'^\| \[(ADR-P\d{3})\]\(#adr-p\d{3}\) \|', line)
        if m: index[m.group(1)].append(n)
    for n, line in enumerate(lines.get(founder, []), 1):
        m = re.match(r'^\| (FD-\d{2}) \|', line)
        if m and line.count('|') >= 5: fd_rows[m.group(1)].append(n)
    for path, ls in lines.items():
        for n, line in enumerate(ls, 1):
            for m in ADR.finditer(line):
                if m.group() not in adr_heads: add('E1', path, n, f'No ADR heading: {m.group()}')
            for m in FD.finditer(line):
                if m.group() not in fd_rows: add('E1', path, n, f'No FD register row: {m.group()}')
    for label, mapping, path in [('ADR heading', adr_heads, decisions), ('ADR anchor', adr_anchors, decisions), ('FD row', fd_rows, founder)]:
        for ident, locs in mapping.items():
            for n in locs[1:]: add('E2', path, n, f'Duplicate {label}: {ident}')
    for ident, locs in adr_heads.items():
        for n in locs:
            if n < 2 or lines[decisions][n-2].strip() != f'<a id="{ident.lower()}"></a>': add('E3', decisions, n, f'Missing/mismatched immediate anchor for {ident}')
            if len(index[ident]) != 1: add('E3', decisions, n, f'Index has {len(index[ident])} entries for {ident}')
    for ident, locs in index.items():
        if ident not in adr_heads:
            for n in locs: add('E3', decisions, n, f'Index entry has no heading: {ident}')
    for ident, locs in adr_anchors.items():
        if ident not in adr_heads:
            for n in locs: add('E3', decisions, n, f'Anchor has no heading: {ident}')
    anchors = {}
    for path, ls in lines.items():
        a = set(); seen = Counter()
        for line in ls:
            for m in re.finditer(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', line, re.I): a.add(m.group(1))
            m = HEADING.match(line)
            if m:
                base = slug(m.group(2)); suffix = seen[base]; seen[base] += 1
                a.add(base + (f'-{suffix}' if suffix else ''))
        anchors[path] = a
    for path, ls in lines.items():
        for n, line in enumerate(ls, 1):
            for m in LINK.finditer(line):
                dest = m.group(1).strip('<>').split(' "')[0]
                if re.match(r'^[a-z][a-z0-9+.-]*:', dest, re.I) or dest.startswith('//'): continue
                target, _, fragment = unquote(dest).partition('#')
                target = (Path(path).parent / target).as_posix() if target else path
                target = __import__('posixpath').normpath(target)
                if target not in docs:
                    if target.endswith('/') and target + 'README.md' in docs: target += 'README.md'
                    elif not target.endswith('.md') and target + '.md' in docs: target += '.md'
                    elif (root / target).is_file(): continue
                    else: add('E4', path, n, f'Missing target: {dest}'); continue
                if fragment and fragment not in anchors[target]:
                    add('E4', path, n, f'Missing anchor: {dest}')
                    add('W3', path, n, f'Anchor may have been renamed: {dest}')
    for path, ls in lines.items():
        for n, line in enumerate(ls, 1):
            m = re.match(r'(?i)^\s*(?:>\s*)?(?:\*\*)?(?:Decision )?Status:(?:\*\*)?\s*(.+)', line)
            if m and not re.search(r'(?i)(?:document|review|checkpoint|artifact|visual direction) status', line):
                value = clean(m.group(1).split('**')[0].split('·')[0].split('|')[0])
                value = value.split(';')[0].strip()
                if value and value.upper() not in STATUSES and not re.match(r'(?i)(?:theo từng mục|see |per |each |depends |not |[A-Z -]+— 20\d\d)', value):
                    # Only decision status declarations are normative; document/review/checkpoint status is separate.
                    if path == decisions and n > min((v[0] for v in adr_heads.values()), default=10**9) and line.lstrip().startswith(('Status:', '**Status:')):
                        add('E5', path, n, f'Invalid decision status: {value}')
            if path == decisions and re.match(r'^\| \[ADR-P\d{3}\]', line):
                value = clean(line.split('|')[-2]).upper()
                if value not in STATUSES: add('E5', path, n, f'Invalid index status: {value}')
    allowfile = root / 'tools/spec-check/allowlist.txt'
    allow = set()
    if allowfile.exists():
        for line in allowfile.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('#'): allow.add(line.strip())
    used = set()
    for path, ls in lines.items():
        for n, line in enumerate(ls, 1):
            matches = []
            for pattern in SECRET: matches.extend(m.group() for m in pattern.finditer(line))
            for m in ENTROPY_TOKEN.finditer(line):
                token = m.group().rstrip('=')
                if '/' in token and (token.startswith('/') or token.count('/') > 1): continue
                freq = Counter(token)
                entropy = -sum(c / len(token) * math.log2(c / len(token)) for c in freq.values())
                if entropy >= 4.3 and re.search(r'[A-Z]', token) and re.search(r'[a-z]', token) and re.search(r'\d', token): matches.append(m.group())
            for token in set(matches):
                entry = f'{path}:{n} {token}'
                if entry in allow: used.add(entry)
                else: add('E6', path, n, f'Potential secret/personal data: {token}')
    for entry in sorted(allow-used): add('W3', 'tools/spec-check/allowlist.txt', 0, f'Unused allowlist entry: {entry}')
    audit = lines.get(decisions, [])
    audit_start = next((i for i, s in enumerate(audit) if re.match(r'^## Contradiction audit', s, re.I)), None)
    audit_end = next((i for i in range(audit_start+1, len(audit)) if audit[i].startswith('## ')), len(audit)) if audit_start is not None else 0
    audit_count = sum(bool(re.match(r'^\| C-\d+ \|', s, re.I)) for s in audit[audit_start:audit_end]) if audit_start is not None else 0
    for path, ls in lines.items():
        for n, line in enumerate(ls, 1):
            for m in COUNT.finditer(line):
                expected = len(adr_heads) if 'adr' in m.group().lower() else audit_count
                if expected and int(m.group(1)) != expected: add('E7', path, n, f'Stated {m.group(1)}, register has {expected}')
    for path, ls in lines.items():
        if path == 'AGENTS.md': continue
        excluded = path.startswith(NON_SPEC_WARNING_PREFIXES)
        def warn(rule, detail):
            nonlocal suppressed_w1_w2
            if excluded: suppressed_w1_w2 += 1
            else: add(rule, path, 1, detail)
        header = '\n'.join(ls[:12])
        if not ls or not ls[0].startswith('# ') or not re.search(r'(?i)(?:status|checkpoint|scope)', header): warn('W1', 'Missing/malformed heading or header metadata')
        m = re.search(r'(?im)^.*Last reviewed\s*:\s*(20\d{2}-\d{2}-\d{2})', '\n'.join(ls[:30]))
        if not m: warn('W2', 'Missing Last reviewed date')
        else:
            try:
                reviewed = dt.date.fromisoformat(m.group(1))
                if (today-reviewed).days > 180: warn('W2', f'Last reviewed {reviewed} is over 180 days old')
            except ValueError: warn('W2', 'Malformed Last reviewed date')
    main = '00-start-here/README.md'
    states = {}
    in_status_table = False
    for line in lines.get(main, []):
        if line.startswith('| Checkpoint | Evidence-backed status |'): in_status_table = True
        if in_status_table and line.startswith('## '): break
        if not in_status_table: continue
        m = re.match(r'^\| (CP[1-8])\b[^|]*\| ([^|]+) \|', line)
        if m and m.group(1) not in states: states[m.group(1)] = m.group(2).strip()
    for path, ls in lines.items():
        if path == main: continue
        for n, line in enumerate(ls, 1):
            m = re.search(r'\b(CP[1-8])\b.{0,70}\b(?:status|is)\s*[:=]?\s*(IN PROGRESS|NOT STARTED|COMPLETE|CLOSED|ACCEPTED|FAILED)\b', line, re.I)
            if m and m.group(1) in states and m.group(2).lower() not in states[m.group(1)].lower():
                add('W4', path, n, f'Claim {m.group(1)} {m.group(2)} differs from README status: {states[m.group(1)]}')
    sorted_findings = sorted(findings, key=lambda x: (list(RULES).index(x['rule']), x['file'], x['line'], x['detail']))
    return (sorted_findings, suppressed_w1_w2) if return_meta else sorted_findings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--format', choices=['text', 'json'], default='text')
    ap.add_argument('--only', choices=RULES)
    args = ap.parse_args()
    found, suppressed = run(args.root, args.only, return_meta=True)
    counts = Counter(f['severity'] for f in found)
    if args.format == 'json': print(json.dumps({'findings': found, 'summary': {'ERROR': counts['ERROR'], 'WARN': counts['WARN'], 'SUPPRESSED_W1_W2': suppressed}}, ensure_ascii=False, indent=2))
    else:
        for rule in RULES:
            group = [f for f in found if f['rule'] == rule]
            if group:
                print(f'\n{rule} ({RULES[rule]}; {len(group)})')
                by_directory = defaultdict(list)
                for f in group: by_directory[str(Path(f['file']).parent)].append(f)
                for directory, items in by_directory.items():
                    print(f'{directory}/')
                    for f in items:
                        excerpt = '<missing Last reviewed>' if rule == 'W2' and f['detail'].startswith('Missing') else f['text']
                        detail = '' if rule in ('W1', 'W2') else f" — {f['detail']}"
                        print(f"  {Path(f['file']).name}:{f['line']}: {excerpt}{detail}")
        print(f"SUMMARY ERROR={counts['ERROR']} WARN={counts['WARN']} SUPPRESSED_W1_W2={suppressed}")
    return int(counts['ERROR'] > 0)

if __name__ == '__main__': sys.exit(main())
