from rest_framework import serializers
from .models import Scrap, ScrapOrder, ScrapCollected

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'

class ScrapOrderSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    scrap_name = serializers.SerializerMethodField()

    class Meta:
        model = ScrapOrder
        fields = '__all__'

    def get_user_username(self, obj):
        return obj.user.username

    def get_scrap_name(self, obj):
        return obj.scrap.name

class ScrapCollectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapCollected
        fields = '__all__'