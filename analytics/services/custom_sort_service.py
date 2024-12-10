from pathlib import Path
from typing import List
import csv


class CustomSortService:
    """Service for custom data type sorting."""

    COLUMN_NAME = 'Typologie des données impactées'

    @classmethod
    def sort_data_types(cls, file_path: Path) -> List[str]:
        """Sort data types from CSV by length and alphabetically."""
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        data_types = set()

        try:
            with open(file_path, encoding='utf-8-sig') as file:
                next(file)  # skip header
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    data_type = str(row[cls.COLUMN_NAME].strip())
                    if data_type:
                        data_types.add(data_type)
        except (csv.Error, KeyError) as e:
            raise ValueError(f"Invalid CSV format: {e}")

        return sorted(data_types, key=lambda x: (len(x), x))
