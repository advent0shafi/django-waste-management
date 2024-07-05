# products/views.py
from rest_framework import viewsets
from .models import Category, Product,  Color, Size, Cart, Order, Return, User, Payment, Refund
from .serializers import CategorySerializer, ProductSerializer, ColorSerializer, SizeSerializer, CartSerializer, OrderSerializer, ReturnSerializer, PaymentSerializer, RefundSerializer
from rest_framework import filters as drf_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as django_filters
from .filters import ProductFilter
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (django_filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer

     @action(detail=True, methods=['patch'])
     def update_status(self, request, pk=None):
        order = self.get_object()
        status = request.data.get('status')
        if status:
            order.status = status
            order.save()
            return Response({'status': 'status updated'})
        else:
            return Response({'error': 'Invalid status'}, status=400)

class ReturnViewSet(viewsets.ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer