from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from analytics.models import EnergyData


@api_view(['GET'])
def export_data(request):
    """Export all energy consumption data"""
    try:
        data = EnergyData.objects.all().order_by('date')
        result = [{
            'date': item.date.strftime('%Y-%m-%d'),
            'region': item.region,
            'consumption': float(item.consumption)
        } for item in data]
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )