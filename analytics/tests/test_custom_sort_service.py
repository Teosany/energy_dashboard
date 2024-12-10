from django.test import TestCase

from analytics.services.custom_sort_service import CustomSortService


class CustomSortServiceTests(TestCase):
    def test_custom_sort_exemple(self):
        """Test sorting by length and then alphabetically"""
        test_data = ["apple", "bat", "zebra", "a", "antelope"]
        result = CustomSortService.custom_sort(test_data)

        expected = ['a', 'bat', 'apple', 'zebra', 'antelope']
        self.assertEqual(result, expected)

    def test_custom_sort(self):
        """Test sorting with real data from CSV file"""
        with open('analytics/static/data/data_types.csv', 'r', encoding='utf-8') as file:
            next(file)
            real_data = set(line.split(';')[2].strip() for line in file)

        result = CustomSortService.custom_sort(list(real_data))

        for i in range(len(result) - 1):
            if len(result[i]) == len(result[i + 1]):
                self.assertLessEqual(result[i], result[i + 1])
            else:
                self.assertLess(len(result[i]), len(result[i + 1]))