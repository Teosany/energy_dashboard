from pathlib import Path

from django.test import TestCase

from analytics.services.custom_sort_service import CustomSortService


class CustomSortServiceTests(TestCase):
    def setUp(self) -> None:
        self.file_path = Path('analytics/static/data/data_types.csv')

    def test_sort_data_types(self):
        result = CustomSortService.sort_data_types(self.file_path)

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, str) for item in result))

        for i in range(len(result) - 1):
            if len(result[i]) == len(result[i + 1]):
                self.assertLessEqual(result[i], result[i + 1])
            else:
                self.assertLess(len(result[i]), len(result[i + 1]))

        expected_type = 'Etat civil (ex : nom, sexe, date de naissance, âge...)'
        self.assertIn(expected_type, result)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            CustomSortService.sort_data_types(Path('nonexistent_file.csv'))