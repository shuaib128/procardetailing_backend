from rest_framework import serializers
from .models import Appointment

# Appointment serilizer
class AppointentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'date',
        )
        model = Appointment