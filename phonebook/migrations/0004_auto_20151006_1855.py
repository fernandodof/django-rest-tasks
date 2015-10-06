# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0003_auto_20151006_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.CharField(default=b'link', max_length=300, blank=True),
        ),
    ]
