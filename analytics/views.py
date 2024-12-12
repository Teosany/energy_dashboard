from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import EnergyData
from .forms import CSVUploadForm
from .services.csv_service import CSVService
from .services.chart_service import ChartService


class HomeView(TemplateView):
    """Main dashboard view for energy consumption data visualization and analysis."""
    template_name = 'analytics/home.html'
    paginate_by = 10

    def get_queryset(self):
        return EnergyData.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        page = self.request.GET.get('page', 1)
        data = Paginator(queryset, self.paginate_by).get_page(page)
        chartData = ChartService.prepare_chart_data(queryset)

        return {
            'upload_form': CSVUploadForm(),
            'energy_data': data,
            **chartData
        }

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            page_num = request.GET.get('page', 1)
            data = Paginator(self.get_queryset(), self.paginate_by).get_page(page_num)

            return JsonResponse({
                'html': render_to_string('analytics/components/table_content.html',
                                         {'energy_data': data}, request),
                'pagination_html': render_to_string('analytics/components/pagination.html',
                                                    {'energy_data': data}, request)
            })
        return super().get(request, *args, **kwargs)

    def post(self, request) -> HttpResponse:
        form = CSVUploadForm(request.POST, request.FILES)
        if not form.is_valid():
            messages.error(request, 'Invalid form data')
            return redirect('analytics:home')

        try:
            records = CSVService.process_file(request.FILES['file'])
            EnergyData.objects.bulk_create([
                EnergyData(**data) for data in records
            ])
            messages.success(request, 'Import ok')
        except Exception as e:
            messages.error(request, f'Import failed: {str(e)}')

        return redirect('analytics:home')
