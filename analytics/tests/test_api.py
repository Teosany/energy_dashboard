from decimal import Decimal
from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from analytics.models import EnergyData


class ApiTests(TestCase):
    def setUp(self):
        EnergyData.objects.create(
            date=datetime(2024, 1, 1),
            region="Île-de-France",
            consumption=Decimal("10.5")
        )

    def test_export_data(self):
        """Test exporting all data"""
        response = self.client.get(reverse('analytics:api:export_data'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(float(response.json()[0]['consumption']), 10.5)