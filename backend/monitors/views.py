from rest_framework import generics

from .serializers import MonitorSerializer

from .models import Monitor


class MonitorListView(generics.ListCreateAPIView):
    serializer_class = MonitorSerializer
    queryset = Monitor.objects.all()


class MonitorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonitorSerializer
    queryset = Monitor.objects.all()
