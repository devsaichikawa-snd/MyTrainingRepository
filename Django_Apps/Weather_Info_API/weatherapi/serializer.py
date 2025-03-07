from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        field = ['id', 'location', 'weather', 'temperature',]
        fields='__all__' # 追加
