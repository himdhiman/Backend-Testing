from django.urls import path, include
from api import views

urlpatterns = [
    path('run/', views.run),
    path('getcode/', views.GetOut),
]