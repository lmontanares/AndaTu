# Generated by Django 3.2.4 on 2021-06-12 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='id_package_2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='package_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
