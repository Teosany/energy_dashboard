from typing import Any, Dict

from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse

from .models import EnergyData
from .forms import CSVUploadForm
from .services.csv_service import CSVService
from .services.chart_service import ChartService


class HomeView(TemplateView):
    """Main dashboard view for energy consumption data visualization and analysis."""
    template_name = 'analytics/home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        queryset = EnergyData.objects.all().order_by('-date')

        context.update({
            'upload_form': CSVUploadForm(),
            'energy_data': self._paginate_queryset(queryset),
            **ChartService.prepare_chart_data(queryset)
        })
        return context

    def post(self, request) -> HttpResponse:
        form = CSVUploadForm(request.POST, request.FILES)
        if not form.is_valid():
            messages.error(request, 'Invalid form data')
            return redirect('analytics:home')

        try:
            with transaction.atomic():
                records = CSVService.process_file(request.FILES['file'])
                EnergyData.objects.bulk_create([
                    EnergyData(**data) for data in records
                ])
            messages.success(request, 'Data imported successfully')
        except Exception as e:
            messages.error(request, f'Import failed: {str(e)}')

        return redirect('analytics:home')

    def _paginate_queryset(self, queryset) -> Any:
        return Paginator(queryset, self.paginate_by).get_page(
            self.request.GET.get('page', 1)
        )