from rest_framework import serializers
from .models import Sumkalar

class SumkalarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sumkalar
        fields = "__all__"
