from django.urls import path, include
from .views import CarListView, AdminCarViewSet, ReservationListCreateView, ReservationDetailView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cars_admin', AdminCarViewSet)


urlpatterns = [
    path('cars/', CarListView.as_view()),
    path('resr/', ReservationListCreateView.as_view()),
    path('resr/<pk>/', ReservationDetailView.as_view()),
]
urlpatterns += router.urls