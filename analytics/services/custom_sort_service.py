from typing import List


class CustomSortService:
    """Service for custom string sorting implementation."""

    @staticmethod
    def custom_sort(strings: List[str]) -> List[str]:
        return sorted(strings, key=lambda x: (len(x), x))