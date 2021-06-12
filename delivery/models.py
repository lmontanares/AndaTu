from django.db import models
from django.utils import timezone
from auth_app.models import User


# Create your models here.

class Delivery(models.Model):
    id_user_A = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender')
    id_user_B = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transport')
    id_package_1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='package_1')
    id_package_2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='package_2', default=None)
    lat_initial = models.FloatField(null=True, max_length=50)
    lng_initial = models.FloatField(null=True, max_length=50)
    lat_final = models.FloatField(null=True, max_length=50)
    lng_final = models.FloatField(null=True, max_length=50)
    date_initial = models.DateTimeField(default=timezone.now)
    date_final = models.DateTimeField(null=True)
    distance = models.FloatField(null=True, max_length=50)
    total = models.FloatField(null=True, max_length=50)


class DeliveryDetail(models.Model):
    id_delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    lat_now = models.FloatField(null=True)
    lng_now = models.FloatField(null=True)
    distance_now = models.FloatField(null=True)
    date_now = models.DateTimeField(default=timezone.now)