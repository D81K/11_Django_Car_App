from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'rent_per_day',
            'available',
            'gear'
        )
    
    # def get_fields(self, *args, **kwargs):
    #     fields = super().get_fields(*args, **kwargs)
        # Ask Rafe for authorization details


class ReservationSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'id',
            'car',
            'start_date',
            'end_date',
            'total_price'
        )
    
    # There must be some validation for reservation dates of the car
    
    def get_total_price(self, obj):
        if obj.start_date and obj.end_date:
            return obj.car.rent_per_day * abs((obj.end_date - obj.start_date).days)
        return obj.car.rent_per_day
