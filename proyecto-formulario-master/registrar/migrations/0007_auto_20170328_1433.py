# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0006_auto_20170328_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='AEM',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False, verbose_name='Sabes lo que es?'),
        ),
    ]
