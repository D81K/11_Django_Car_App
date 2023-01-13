from django.shortcuts import render
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet



# Create your views here.

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # permission_classes = [IsAdminUser]
    # permission_classes = (IsAuthenticated, )

class AdminCarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser, )

class ReservationListCreateView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the reservations to staff members
        and the reservations of the current user.
        """
        queryset = super().get_queryset()
        
        # print(self.request)
        # print(self.request.user)
        # print(self.request.method)
        # print(self.request.COOKIES)

        if self.request.user.is_staff:
            return queryset
        return Reservation.objects.filter(customer = self.request.user)
    

class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the reservations to staff members
        and the reservations of the current user.
        """
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return Reservation.objects.filter(customer = self.request.user)
