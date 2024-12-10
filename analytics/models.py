from decimal import Decimal, DecimalException

from django.db import models
from django.core.exceptions import ValidationError


class EnergyData(models.Model):
    date = models.DateField()
    region = models.CharField(max_length=100)
    consumption = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Use comma as decimal separator (e.g., 42,5)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = "Energy Data"
        ordering = ['-date', 'region']
        indexes = [
            models.Index(fields=['date', 'region']),
            models.Index(fields=['region']),
        ]

    def get_formatted_consumption(self) -> str:
        """French formatted consumption value with comma"""
        return f"{self.consumption}".replace('.', ',') + " TWh"

    get_formatted_consumption.short_description = 'Consumption (TWh)'

    def clean(self) -> None:
        """Convert comma to dot in consumption value"""
        if isinstance(self.consumption, str):
            try:
                self.consumption = Decimal(self.consumption.replace(',', '.'))
            except (ValueError, DecimalException):
                raise ValidationError({
                    'consumption': "Invalid number format. Use comma as decimal separator (e.g., 42,5)"
                })