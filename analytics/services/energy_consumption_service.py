import csv
from decimal import Decimal
from typing import Dict, Any


class EnergyConsumptionService:
    """Service for analyzing French energy consumption data."""

    @staticmethod
    def find_peak_consumption(file_path: str) -> Dict[str, Any]:
        peak_info = {"region": "", "date": "", "consumption": Decimal('0')}

        with open(file_path, encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                consumption = Decimal(row['Valeur (TWh)'].strip().replace(',', '.'))
                if consumption > peak_info['consumption']:
                    peak_info.update({
                        'region': row['Region'].strip('"'),
                        'date': row['Date'].strip(),
                        'consumption': consumption
                    })

        return {**peak_info, 'consumption': float(peak_info['consumption'])}