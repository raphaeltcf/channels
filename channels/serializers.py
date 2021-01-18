# channels/serializers.py

from rest_framework import serializers

from channels.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "description",
            "link",
            "title",
        ]