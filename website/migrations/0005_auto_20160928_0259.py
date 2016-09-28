# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160823_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='degree',
            field=models.CharField(choices=[('BSC', 'Bachelor'), ('MSC', 'Master Deutsch'), ('DSS', 'Distributed Software Systems'), ('JBA', 'Joint-Bachelor of Arts'), ('EDU', 'Lehramt Bachelor of Education')], max_length=3, unique=True, verbose_name='Abschluss'),
        ),
    ]
