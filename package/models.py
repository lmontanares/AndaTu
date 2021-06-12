from django.db import models

from auth_app.models import User


class Package(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    content = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    weight = models.FloatField()

    REQUIRED_FIELDS = ['content', 'weight']
