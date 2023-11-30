from django.urls import path
from rest_framework import routers

from .views import ApiViewRequest

router = routers.SimpleRouter()
urlpatterns = [
    path("sumar/", ApiViewRequest.as_view(), name="pets"),

]
