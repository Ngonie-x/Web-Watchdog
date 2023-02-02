from rest_framework import generics

from .serializers import MonitorSerializer


class MonitorListView(generics.ListCreateAPIView):
    serializer_class = MonitorSerializer


class MonitorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonitorSerializer
