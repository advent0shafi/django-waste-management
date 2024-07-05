from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Scrap, ScrapOrder, ScrapCollected
from .serializers import ScrapSerializer, ScrapOrderSerializer, ScrapCollectedSerializer

class ScrapViewSet(viewsets.ModelViewSet):
    
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer

class ScrapOrderViewSet(viewsets.ModelViewSet):
    queryset = ScrapOrder.objects.all()
    serializer_class = ScrapOrderSerializer

class ScrapCollectedViewSet(viewsets.ModelViewSet):
    queryset = ScrapCollected.objects.all()
    serializer_class = ScrapCollectedSerializer
