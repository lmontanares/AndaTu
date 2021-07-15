from rest_framework import serializers

from .models import DeliveryDetail, Delivery


class DeliveryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetail
        fields = ['id_delivery', 'lat_now', 'lng_now', 'distance_now', 'date_now']


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'id_user_A', 'id_user_B', 'id_package_1', 'phone_receiver', 'name_receiver', 'metro_init',
                  'metro_final', 'date_initial', 'date_final', 'distance', 'payment', 'status']
