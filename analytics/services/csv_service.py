import csv
from datetime import datetime
from io import StringIO
from typing import Iterator


class CSVService:
    @staticmethod
    def process_file(file) -> Iterator[dict]:
        """Process CSV file and yield data for each row"""
        csv_data = csv.DictReader(
            StringIO(file.read().decode('utf-8-sig')),
            delimiter=';'
        )

        for row in csv_data:
            yield {
                'date': datetime.strptime(row['Date'].strip(), '%Y').date(),
                'region': row['Region'].strip('"'),
                'consumption': float(row['Valeur (TWh)'].strip().replace(',', '.'))
            }