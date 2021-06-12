
from rest_framework import viewsets

from .models import Delivery, DeliveryDetail
from .serializers import DeliverySerializer, DeliveryDetailSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer



class DeliveryDetailViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDetail.objects.all()
    serializer_class = DeliveryDetailSerializer
