# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0004_auto_20170327_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='bulto',
            new_name='bulto_pecho',
        ),
        migrations.AddField(
            model_name='persona',
            name='problema_mama',
            field=models.CharField(blank=True, choices=[('R', 'REGULARMENTE'), ('A', 'A veces'), ('NU', 'NUNCA')], default='R', max_length=1, null=True),
        ),
    ]
