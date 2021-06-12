# Generated by Django 3.2.4 on 2021-06-12 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_initial', models.FloatField(max_length=50, null=True)),
                ('lng_initial', models.FloatField(max_length=50, null=True)),
                ('lat_final', models.FloatField(max_length=50, null=True)),
                ('lng_final', models.FloatField(max_length=50, null=True)),
                ('date_initial', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_final', models.DateTimeField(null=True)),
                ('distance', models.FloatField(max_length=50, null=True)),
                ('total', models.FloatField(max_length=50, null=True)),
                ('id_package_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_1', to=settings.AUTH_USER_MODEL)),
                ('id_package_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_2', to=settings.AUTH_USER_MODEL)),
                ('id_user_A', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('id_user_B', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transport', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_now', models.FloatField(null=True)),
                ('lng_now', models.FloatField(null=True)),
                ('distance_now', models.FloatField(null=True)),
                ('date_now', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='delivery.delivery')),
            ],
        ),
    ]
