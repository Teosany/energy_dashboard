from django.contrib import admin

from .models import EnergyData

@admin.register(EnergyData)
class EnergyDataAdmin(admin.ModelAdmin):
    list_display = ('region', 'date', 'get_formatted_consumption', 'created_at')
    list_filter = ('region', 'date')
    search_fields = ('region',)
    date_hierarchy = 'date'
    ordering = ('-date', '-consumption')