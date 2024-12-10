from django.urls import path, include

from . import views


app_name = 'analytics'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/', include('analytics.api.urls', namespace='api')),
]
