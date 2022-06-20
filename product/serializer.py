from rest_framework import serializers
from .models import Event as EventModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"

