
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from passengers.views import PassengerViewset

router = SimpleRouter()

router.register(r'passengers',PassengerViewset, 'passengers')

urlpatterns = router.urls
