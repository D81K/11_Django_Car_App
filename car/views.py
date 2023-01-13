from django.shortcuts import render
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q



# Create your views here.

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_fields = ['brand', 'model']
    search_fields = ['brand', 'model']

    def get_queryset(self):
        """
        This view should return a list of available cars
        to all users and a list of all cars (available or not) to staff members.
        """
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(availability=True)

        # https://www.django-rest-framework.org/api-guide/requests/#query_params
        # get start and end dates from request object
        # request.query_params is a more correctly named synonym for request.GET
        # any HTTP method type may include query parameters, not just GET
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        # if there is a start and end date coming inside request and it is valid
        if start is not None and end is not None and start < end:

            # https://docs.djangoproject.com/en/4.1/topics/db/queries/#complex-lookups-with-q-objects
            condition_1 = Q(start_date__lte=end)
            condition_2 = Q(end_date__gte=start)

            # Django values_list() is an optimization to grab specific data from the database 
            # instead of building and loading the entire model instance. 
            available = Reservation.objects.filter(
                condition_1 & condition_2).values_list('car_id', flat=True)
            # When grabbing a single values from the db, you can pass`flat=true` 
            # which will just give you back single values, instead of tuples

            queryset.filter(id__in=available)

        return queryset

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
