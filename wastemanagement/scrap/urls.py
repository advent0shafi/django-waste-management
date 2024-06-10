from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScrapViewSet, ScrapOrderViewSet, ScrapCollectedViewSet

router = DefaultRouter()
router.register(r'scraps', ScrapViewSet)
router.register(r'scrap-orders', ScrapOrderViewSet)
router.register(r'scrap-collected', ScrapCollectedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
