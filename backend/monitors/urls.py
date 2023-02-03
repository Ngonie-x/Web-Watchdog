from django.urls import path
from . import views

urlpatterns = [
    path("", views.MonitorListView.as_view()),
    path("get-monitor/", views.MonitorListView.as_view()),

]
