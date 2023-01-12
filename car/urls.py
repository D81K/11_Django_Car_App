from django.urls import path, include
from .views import CarListView

urlpatterns = [
    path('cars/', CarListView.as_view()),
    
]