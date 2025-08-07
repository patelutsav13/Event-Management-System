from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_event, name='view_events'),
]
