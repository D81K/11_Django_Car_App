from django.shortcuts import render
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet



# Create your views here.

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # permission_classes = [IsAdminUser]
    # permission_classes = (IsAuthenticated, )

class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class AdminCarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser, )