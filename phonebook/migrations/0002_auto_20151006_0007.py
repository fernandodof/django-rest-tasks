# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=6),
        ),
    ]
