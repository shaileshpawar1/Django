from rest_framework import serializers
from .models import *


class StudSerializers(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = '__all__'
