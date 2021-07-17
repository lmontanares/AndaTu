# Generated by Django 3.2.4 on 2021-07-17 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
        ('delivery', '0008_auto_20210715_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='id_package_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_1', to='package.package'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(default='pendiente', max_length=20),
        ),
    ]
