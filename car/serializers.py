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
            'gaer',
            'rent_per_day',
            'availability',
        )

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')

        if request.user and not request.user.is_staff:
            fields.pop('plate_number', None)
            fields.pop('availability', None)
        return fields


class ReservationSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'id',
            'customer',
            'car',
            'start_date',
            'end_date',
            'total_price',
        )

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('customer', 'start_date', 'end_date'),
                message=("You already have a reservation between this dates..")
            )
        ]

    def get_total_price(self, obj):
        if obj.start_date and obj.end_date:
            return obj.car.rent_per_day * abs((obj.end_date-obj.start_date).days)
        return obj.car.rent_per_day