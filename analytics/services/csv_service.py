import csv
from datetime import datetime, date
from decimal import Decimal
from io import StringIO
from typing import Iterator, Dict, Union

from django.core.files.uploadedfile import UploadedFile


class CSVService:
    @staticmethod
    def process_file(file: UploadedFile) -> Iterator[Dict[str, Union[date, str, float]]]:
        """Process CSV file and yield data for each row"""
        csv_data = csv.DictReader(
            StringIO(file.read().decode('utf-8-sig')),
            delimiter=';'
        )

        for row in csv_data:
            yield {
                'date': datetime.strptime(row['Date'].strip(), '%Y').date(),
                'region': row['Region'].strip('"'),
                'consumption': Decimal(row['Valeur (TWh)'].strip().replace(',', '.'))
            }