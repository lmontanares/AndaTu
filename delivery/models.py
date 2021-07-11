from django.db import models
from django.utils import timezone
from auth_app.models import User


# Create your models here.

class Delivery(models.Model):
    id_user_A = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender')
    id_user_B = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transport', blank=True)
    id_package_1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='package_1')
    phone_receiver = models.CharField(max_length=20)
    name_receiver = models.CharField(max_length=20)
    metro_init = models.CharField(max_length=20)
    metro_final = models.CharField(max_length=20)
    #id_package_2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='package_2', default=None)
    #lat_initial = models.FloatField(null=True, max_length=50)
    #lng_initial = models.FloatField(null=True, max_length=50)
    #lat_final = models.FloatField(null=True, max_length=50)
    #lng_final = models.FloatField(null=True, max_length=50)
    date_initial = models.DateTimeField(default=timezone.now)
    date_final = models.DateTimeField(null=True)
    distance = models.FloatField(null=True, max_length=50)
    payment = models.FloatField(null=True, max_length=50)
    status = models.CharField(max_length=20, default='activo')


class DeliveryDetail(models.Model):
    id_delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    lat_now = models.FloatField(null=True)
    lng_now = models.FloatField(null=True)
    distance_now = models.FloatField(null=True)
    date_now = models.DateTimeField(default=timezone.now)
