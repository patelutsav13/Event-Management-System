from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('upcoming/', views.up_events , name = 'upcoming'),
]
