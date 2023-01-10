from django.contrib import admin
from .models import Car, Reservation


# Register your models here.

admin.site.register(Car)
admin.site.register(Reservation)

admin.site.site_title = 'Car Reservation App'
admin.site.site_header = 'Rent Car Admin Portal'
admin.site.index_title = 'Welcome'