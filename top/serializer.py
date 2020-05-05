from .models import ApiVieu
from rest_framework import serializers


class ApiVieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiVieu
        fields = "__all__"