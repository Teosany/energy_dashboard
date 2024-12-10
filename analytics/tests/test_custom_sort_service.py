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
        with open('analytics/static/data/data_types.csv', 'r', encoding='utf-8-sig') as file:
            next(file);next(file)

            typologies = set()
            for line in file:
                if line.strip():
                    column = line.split(';')[4]
                    types = [t.strip() for t in column.split('"),') if t.strip()]
                    types = [t + '")' if t.count('(') > t.count(')') else t for t in types]
                    typologies.update(types)

        result = CustomSortService.custom_sort(list(typologies))

        for item in result:
            print(f"Len {len(item)}: {item}")

        for i in range(len(result) - 1):
            if len(result[i]) == len(result[i + 1]):
                self.assertLessEqual(result[i], result[i + 1])
            else:
                self.assertLess(len(result[i]), len(result[i + 1]))