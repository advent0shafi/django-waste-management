from rest_framework import serializers
from .models import Scrap, ScrapOrder, ScrapCollected

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'

class ScrapOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapOrder
        fields = '__all__'

class ScrapCollectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapCollected
        fields = '__all__'
