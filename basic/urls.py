from django.urls import include, path

from rest_framework import routers
from channels.api import ChannelViewSet

api_router = routers.DefaultRouter()
api_router.register(r"channels", ChannelViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]