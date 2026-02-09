from rest_framework import serializers
from .models import Client

class ClinetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"