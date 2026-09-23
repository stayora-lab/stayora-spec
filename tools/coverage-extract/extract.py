#!/usr/bin/env python3
"""Extract lexical prototype evidence at one explicit immutable commit."""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = 'https://github.com/stayora-lab/stayora-new.git'
TEST_CALL = re.compile(r'\b(?:describe|it|test)(?:\.skip|\.only)?\s*\(\s*(["\'`])([^"\'`\n]+)\1')
EXPORTED_FUNCTION = re.compile(r'^\s*export\s+(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(')
CONSTANT = re.compile(r'^\s*(?:export\s+)?const\s+([A-Za-z_$][\w$]*)\s*=\s*(.+?);\s*$')
TYPE = re.compile(r'^\s*export\s+type\s+([A-Za-z_$][\w$]*)\s*=\s*(.*)')
QUOTED = re.compile(r'["\']([^"\']+)["\']')
LIFECYCLE_NAME = re.compile(r'(?:Status|Kind|Outcome|Reason|Origin|Basis)$')


def command(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip()


def load_mapping(path):
    raw = '\n'.join(line for line in Path(path).read_text(encoding='utf-8').splitlines() if not line.lstrip().startswith('#'))
    data = json.loads(raw)
    rows = data['guardrails']
    if set(rows) != {str(n) for n in range(1, 20)}:
        raise ValueError('Mapping must have exactly guardrails 1–19')
    for row in rows.values():
        if not row.get('name') or not isinstance(row.get('patterns'), list): raise ValueError('Each guardrail needs a name and pattern list')
    return data


def extract(prototype, mapping):
    prototype = Path(prototype)
    missing = [p for p in mapping['expected_files'] if not (prototype / p).is_file()]
    tests, functions, assumptions, states = [], [], [], []
    domain = prototype / 'src/lib/domain'
    for path in sorted(domain.rglob('*.test.ts')) if domain.exists() else []:
        rel = path.relative_to(prototype).as_posix()
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            match = TEST_CALL.search(line)
            if match and re.search(r'\b(?:it|test)(?:\.skip|\.only)?\s*\(', line):
                tests.append({'kind': 'test', 'name': match.group(2), 'file': rel, 'line': number})
    engine = domain / 'engine.ts'
    if engine.exists():
        for number, line in enumerate(engine.read_text(encoding='utf-8').splitlines(), 1):
            match = EXPORTED_FUNCTION.match(line)
            if match: functions.append({'kind': 'function', 'name': match.group(1), 'file': 'src/lib/domain/engine.ts', 'line': number})
    config = domain / 'config.ts'
    if config.exists():
        for number, line in enumerate(config.read_text(encoding='utf-8').splitlines(), 1):
            match = CONSTANT.match(line)
            if match: assumptions.append({'name': match.group(1), 'value': match.group(2), 'file': 'src/lib/domain/config.ts', 'line': number})
    types = domain / 'types.ts'
    if types.exists():
        lines = types.read_text(encoding='utf-8').splitlines()
        for number, line in enumerate(lines, 1):
            match = TYPE.match(line)
            if not match or not LIFECYCLE_NAME.search(match.group(1)): continue
            declaration = match.group(2)
            cursor = number
            while ';' not in declaration and cursor < len(lines):
                declaration += ' ' + lines[cursor].strip()
                cursor += 1
            values = QUOTED.findall(declaration.split(';')[0])
            if values: states.append({'name': match.group(1), 'values': values, 'file': 'src/lib/domain/types.ts', 'line': number})
        owner = None
        for number, line in enumerate(lines, 1):
            match = re.match(r'^export type (\w+) = \{', line)
            if match: owner = match.group(1)
            if owner and re.search(r'\bstatus:\s*["\']', line):
                values = QUOTED.findall(line)
                if len(values) > 1: states.append({'name': f'{owner}.status', 'values': values, 'file': 'src/lib/domain/types.ts', 'line': number})
            if owner and line.strip() == '};': owner = None
    return {'missing': missing, 'tests': tests, 'functions': functions, 'assumptions': assumptions, 'states': states}


def matched(name, patterns):
    for pattern in patterns:
        if pattern.startswith('re:'):
            if re.search(pattern[3:], name, re.I): return True
        elif pattern.casefold() in name.casefold(): return True
    return False


def md_cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def render(data, mapping, sha, spec_commit, timestamp):
    out = [f'# Coverage evidence — {sha}', '', 'Prototype repository: `stayora-lab/stayora-new`  ', f'Prototype SHA: `{sha}`  ', f'Extraction timestamp (UTC): `{timestamp}`  ', f'Spec commit containing mapping: `{spec_commit}`', '', 'Generated evidence. Not canonical. Coverage states are assigned by the Product Architect.', '', '## 1. Guardrail evidence', '']
    if data['missing']:
        out += ['Expected files missing at this SHA:'] + [f'- `{path}`' for path in data['missing']] + ['']
    material = data['tests'] + data['functions']
    mapped = set()
    for number in range(1, 20):
        row = mapping['guardrails'][str(number)]
        out += [f"### {number}. {row['name']}", '']
        found = [(index, item) for index, item in enumerate(material) if matched(item['name'], row['patterns'])]
        if not found: out += ['No matching evidence found at this SHA.', '']
        else:
            for index, item in found:
                mapped.add(index)
                out.append(f"- {item['kind'].title()}: `{item['name']}` — `{item['file']}:{item['line']}`")
            out.append('')
    out += ['## 2. Prototype assumptions found', '', '| Name | Value | File:line |', '|---|---|---|']
    for item in data['assumptions']:
        out.append(f"| `{md_cell(item['name'])}` | `{md_cell(item['value'])}` | `{item['file']}:{item['line']}` |")
    if not data['assumptions']: out.append('| None found | — | — |')
    out += ['', '## 3. Lifecycle states found', '']
    for item in data['states']:
        out += [f"### {item['name']}", '', f"`{item['file']}:{item['line']}` — " + ', '.join(f'`{md_cell(value)}`' for value in item['values']), '']
    if not data['states']: out += ['No lifecycle state unions found.', '']
    out += ['## 4. Unmapped material', '', 'Tests and exported engine functions that matched no guardrail pattern:', '']
    for index, item in enumerate(material):
        if index not in mapped: out.append(f"- {item['kind'].title()}: `{item['name']}` — `{item['file']}:{item['line']}`")
    if len(mapped) == len(material): out.append('No unmapped tests or exported engine functions.')
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sha', help='Explicit prototype commit SHA (full SHA for remote fetch)')
    parser.add_argument('--prototype-dir', help='Read-only local checkout at the requested SHA; avoids network')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-fA-F]{7,40}', args.sha): parser.error('SHA must be 7–40 hexadecimal characters')
    root = Path(__file__).resolve().parents[2]
    mapping = load_mapping(root / 'tools/coverage-extract/guardrails.yml')
    spec_commit = command('git', 'rev-parse', 'HEAD', cwd=root)
    if args.prototype_dir:
        prototype = Path(args.prototype_dir).resolve()
        full_sha = command('git', 'rev-parse', 'HEAD', cwd=prototype)
        if not full_sha.startswith(args.sha.lower()): parser.error('Local checkout HEAD does not match requested SHA')
        data = extract(prototype, mapping)
    else:
        if len(args.sha) != 40: parser.error('Remote fetch requires a full 40-character SHA; short SHA works with --prototype-dir')
        with tempfile.TemporaryDirectory(prefix='coverage-extract-') as directory:
            command('git', 'init', '-q', directory)
            command('git', 'fetch', '--depth=1', REPO, args.sha.lower(), cwd=directory)
            full_sha = command('git', 'rev-parse', 'FETCH_HEAD', cwd=directory)
            if full_sha != args.sha.lower(): raise RuntimeError('Fetched commit does not match requested SHA')
            command('git', 'checkout', '--detach', 'FETCH_HEAD', cwd=directory)
            data = extract(directory, mapping)
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    report = render(data, mapping, full_sha, spec_commit, timestamp)
    destination = root / 'generated/coverage' / f'{full_sha[:7]}.md'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report, encoding='utf-8')
    print(destination.relative_to(root))
    return 0

if __name__ == '__main__': sys.exit(main())
