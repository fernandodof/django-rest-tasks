# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_auto_20151006_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
