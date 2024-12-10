from pathlib import Path
from decimal import Decimal
from typing import Dict, Union
import csv


class EnergyConsumptionService:
    @classmethod
    def find_peak_consumption(cls, file_path: Path) -> Dict[str, Union[str, float]]:
        """Find the peak electricity consumption by region"""
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        peak_info = {"region": "", "date": "", "consumption": Decimal('0')}

        try:
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
        except KeyError:
            raise ValueError("Required columns not found in CSV")
        except csv.Error as e:
            raise ValueError(f"Invalid CSV format: {e}")

        return {**peak_info, 'consumption': float(peak_info['consumption'])}