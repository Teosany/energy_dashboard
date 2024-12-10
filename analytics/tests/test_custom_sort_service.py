from django.test import TestCase

from analytics.services.custom_sort_service import CustomSortService


class CustomSortServiceTests(TestCase):
    def test_custom_sort(self):
        """Test sorting by length and then alphabetically"""
        test_data = ["apple", "bat", "zebra", "a", "antelope"]
        result = CustomSortService.custom_sort(test_data)

        expected = ['a', 'bat', 'apple', 'zebra', 'antelope']
        self.assertEqual(result, expected)