from pathlib import Path

from django.test import TestCase

from analytics.services.energy_consumption_service import EnergyConsumptionService


class EnergyConsumptionServiceTests(TestCase):
    def setUp(self) -> None:
        self.file_path = Path('analytics/static/data/consumption_by_region.csv')

    def test_find_peak_consumption(self):
        result = EnergyConsumptionService.find_peak_consumption(self.file_path)

        for field in ['region', 'date', 'consumption']:
            self.assertIn(field, result)
            self.assertIsInstance(result[field], str if field != 'consumption' else float)

        self.assertEqual(result['region'], 'Île-de-France')
        self.assertEqual(result['date'], '2016')
        self.assertEqual(result['consumption'], 74.0)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            EnergyConsumptionService.find_peak_consumption(Path('nonexistent_file.csv'))