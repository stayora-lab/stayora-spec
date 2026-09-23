import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('spec_check', HERE / 'check.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
CASES = json.loads((Path(__file__).parent / 'fixtures/cases.json').read_text())

class Rules(unittest.TestCase):
    def base(self, root):
        decision = root / '00-start-here/DECISIONS.md'
        decision.parent.mkdir(parents=True)
        decision.write_text('# Decisions\n> Status: DRAFT\nLast reviewed: 2026-09-23\n| [ADR-P001](#adr-p001) | One | CONFIRMED |\n<a id="adr-p001"></a>\n### ADR-P001 — One\n**Status: CONFIRMED**\n## Contradiction audit\n| C-01 | One | X | OPEN |\n')
        fd = root / '11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md'
        fd.parent.mkdir(parents=True)
        fd.write_text('# Founder decisions\n> Status: DRAFT\nLast reviewed: 2026-09-23\n| FD-01 | One | CLOSED | Open |\n')
        readme = root / '00-start-here/README.md'
        readme.write_text('# Status\n> Status: DRAFT\nLast reviewed: 2026-09-23\n| Checkpoint | Evidence-backed status |\n|---|---|\n| CP8 — UX | IN PROGRESS |\n')
        sample = root / 'sample.md'
        sample.write_text('# Sample\n> Status: DRAFT\nLast reviewed: 2026-09-23\n')
        return sample, decision

    def test_warning_scope_and_secret_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.base(root)
            fixture_root = Path(__file__).parent / 'fixtures'
            for folder, filename in [('generated', 'evidence.md'), ('tools', 'evidence.md'), ('.github', 'evidence.md'), ('spec', 'chapter.md')]:
                target = root / folder / filename
                target.parent.mkdir(parents=True)
                fixture_folder = folder if folder == 'spec' else 'generated'
                target.write_text((fixture_root / fixture_folder / filename.replace('.md', '.txt')).read_text())
            findings, suppressed = checker.run(root, today=__import__('datetime').date(2026, 9, 23), return_meta=True)
            self.assertEqual(suppressed, 6)
            self.assertFalse(any(f['file'].startswith(('generated/', 'tools/', '.github/')) and f['rule'] in ('W1', 'W2') for f in findings))
            self.assertEqual({f['rule'] for f in findings if f['file'] == 'spec/chapter.md'}, {'W1', 'W2'})
            for folder in ('generated', 'tools', '.github'):
                with (root / folder / 'evidence.md').open('a') as stream:
                    stream.write('Contact test@example.com\n')
            findings = checker.run(root, only='E6')
            self.assertEqual({f['file'] for f in findings}, {f'{folder}/evidence.md' for folder in ('generated', 'tools', '.github')})

    def test_fixture_cases(self):
        for rule, cases in CASES.items():
            for outcome, content in cases.items():
                with self.subTest(rule=rule, outcome=outcome), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    sample, decision = self.base(root)
                    if rule == 'E2':
                        decision.write_text(decision.read_text().replace('<a id="adr-p001"></a>\n### ADR-P001 — One', content))
                    elif rule == 'E3':
                        decision.write_text(decision.read_text().replace('<a id="adr-p001"></a>\n### ADR-P001 — One', content))
                    elif rule == 'W2':
                        sample.write_text(sample.read_text().replace('Last reviewed: 2026-09-23', content))
                    elif rule == 'E5':
                        decision.write_text(decision.read_text().replace('**Status: CONFIRMED**', content))
                    else:
                        sample.write_text(content + '\n' if rule == 'W1' else sample.read_text() + content + '\n')
                    got = checker.run(root, rule, today=__import__('datetime').date(2026, 9, 23))
                    self.assertEqual(bool(got), outcome == 'fail', (rule, outcome, got[:2]))

if __name__ == '__main__': unittest.main()
