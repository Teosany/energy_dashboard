import json
from typing import Dict

from django.db.models import Sum, QuerySet


class ChartService:
    @staticmethod
    def prepare_chart_data(queryset: QuerySet) -> Dict[str, str]:
        """Prepare data for chart visualization"""
        regions_data = queryset.values('region').annotate(
            total=Sum('consumption')
        ).order_by('-total')

        years_data = queryset.values('date').annotate(
            total=Sum('consumption')
        ).order_by('date')

        return {
            'region_labels': json.dumps([d['region'].strip('"') for d in regions_data]),
            'region_values': json.dumps([float(str(d['total'])) for d in regions_data]),
            'year_labels': json.dumps([d['date'].strftime('%Y') for d in years_data]),
            'year_values': json.dumps([float(str(d['total'])) for d in years_data])
        }