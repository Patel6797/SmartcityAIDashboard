from django.urls import path
from .views import SensorDataListCreateView, index

urlpatterns = [
    path('', index, name='index'),  # For the frontend
    path('data/', SensorDataListCreateView.as_view(), name='sensor-data-list-create'),  # For the API
]
