from django.urls import path, include
from secondapp import views

urlpatterns = [
    path('hos/', views.hos)
]
