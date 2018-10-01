# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0001_initial'),
        ('places', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('site', models.URLField(blank=True)),
                ('city', models.ForeignKey(to='places.City')),
                ('employee', models.ManyToManyField(to='contacts.Contact')),
                ('owner', models.ForeignKey(related_name='owner_shops', to='contacts.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_type',
            field=models.ForeignKey(to='shops.ShopType'),
        ),
        migrations.AddField(
            model_name='shop',
            name='warehouses',
            field=models.ManyToManyField(to='warehouses.Warehouse'),
        ),
    ]
