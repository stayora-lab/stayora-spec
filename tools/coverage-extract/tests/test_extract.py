import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('coverage_extract', ROOT / 'extract.py')
extractor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractor)
FIXTURE = Path(__file__).parent / 'fixtures/prototype'

class ExtractionTests(unittest.TestCase):
    def setUp(self):
        self.mapping = extractor.load_mapping(ROOT / 'guardrails.yml')

    def test_mapping_has_exact_21_rows(self):
        self.assertEqual(list(self.mapping['guardrails']), [str(i) for i in range(1, 22)])

    def test_lexical_extraction_and_unmapped_material(self):
        data = extractor.extract(FIXTURE, self.mapping)
        self.assertEqual(data['missing'], [])
        self.assertEqual([(x['name'], x['line']) for x in data['tests']], [('request differs from Booking', 2), ('new unmapped behavior', 3), ('an active grant is the role; a client-sent role is ignored', 2)])
        self.assertEqual([x['name'] for x in data['functions']], ['createRequest', 'resolveConflict', 'newBehavior', 'resolveWorkingRole'])
        self.assertEqual(data['assumptions'][0]['value'], '30 * 60 * 1000')
        self.assertIn('COMPLETED', data['states'][0]['values'])
        self.assertTrue(any(x['name'] == 'Booking.status' for x in data['states']))
        output = extractor.render(data, self.mapping, 'a'*40, 'b'*40, '2026-09-23T00:00:00Z')
        self.assertIn('No matching evidence found at this SHA.', output)
        self.assertIn('new unmapped behavior', output.split('## 4. Unmapped material')[1])
        self.assertIn('newBehavior', output.split('## 4. Unmapped material')[1])
        self.assertIn('Generated evidence. Not canonical.', output)
        self.assertNotIn('TESTED — PASS', output)
        self.assertNotIn('VALIDATED ELSEWHERE', output)
        row18 = output.split('### 18.')[1].split('### 19.')[0]
        self.assertIn('an active grant is the role; a client-sent role is ignored', row18)
        self.assertIn('resolveWorkingRole', row18)
        self.assertNotIn('No matching evidence found at this SHA.', row18)

    def test_missing_expected_file_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            data = extractor.extract(directory, self.mapping)
            self.assertEqual(len(data['missing']), 6)
            output = extractor.render(data, self.mapping, 'a'*40, 'b'*40, '2026-09-23T00:00:00Z')
            self.assertIn('Expected files missing at this SHA:', output)
            self.assertIn('src/lib/domain/engine.ts', output)

    def test_literal_and_regex_patterns(self):
        self.assertTrue(extractor.matched('Late SUCCEEDED', ['late succeeded']))
        self.assertTrue(extractor.matched('checkout then completion', ['re:checkout.*completion']))
        self.assertFalse(extractor.matched('checkOutStay', ['checkout.*completion']))

if __name__ == '__main__': unittest.main()
