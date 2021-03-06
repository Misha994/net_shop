# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('gender', models.SmallIntegerField(choices=[(0, 'man'), (1, 'female')])),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
