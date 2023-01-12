from django.urls import path, include
from .views import CarListView, AdminCarViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cars_admin', AdminCarViewSet)


urlpatterns = [
    path('cars/', CarListView.as_view()),
]
urlpatterns += router.urls