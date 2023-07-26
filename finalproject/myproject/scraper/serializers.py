from rest_framework import serializers
from .models import StockData


class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = ['symbol', 'name', 'last_price', 'change', 'percentage_change']
