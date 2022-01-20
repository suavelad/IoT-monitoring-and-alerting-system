import datetime

from rest_framework import serializers

from .models import Log
from rest_framework.generics import get_object_or_404


class LogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Log
        fields = ('__all__')
        read_only_fields = ('is_active', 'is_staff')


class SendEmailSerializer( serializers.Serializer):
    senders  = serializers.ListField(child=serializers.EmailField())
    # sender =serializers.EmailField(required=True)
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)