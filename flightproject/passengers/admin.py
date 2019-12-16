from django.contrib import admin

# Register your models here.
from .models import PassengersModel, FlightsModel

admin.site.register(PassengersModel)
admin.site.register(FlightsModel)