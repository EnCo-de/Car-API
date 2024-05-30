from django.contrib import admin
from .models import Car, Category, Manufacturer

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Manufacturer)