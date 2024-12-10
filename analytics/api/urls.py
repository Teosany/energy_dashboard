from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('export/', views.export_data, name='export_data'),
]