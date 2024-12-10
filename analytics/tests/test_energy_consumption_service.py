from django.test import TestCase

from analytics.services.energy_consumption_service import EnergyConsumptionService


class EnergyConsumptionServiceTests(TestCase):
    def test_find_peak_consumption(self):
        """Test finding peak consumption from sample data"""
        result = EnergyConsumptionService.find_peak_consumption(
            'analytics/static/data/consumption_by_region.csv'
        )

        self.assertEqual(result['region'], 'Île-de-France')
        self.assertEqual(result['date'], '2016')
        self.assertEqual(result['consumption'], 74.0)