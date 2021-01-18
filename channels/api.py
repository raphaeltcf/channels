from rest_framework import viewsets

from channels.models import Channel
from channels.serializers import ChannelSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer