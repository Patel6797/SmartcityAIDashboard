from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer
from django.shortcuts import render

# API view to list and create sensor data
class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all().order_by('-timestamp')
    serializer_class = SensorDataSerializer

# View to render the index page
def index(request):
    return render(request, 'dashboard/index.html')
