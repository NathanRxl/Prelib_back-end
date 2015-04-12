# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_auto_20150404_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='available_bikes',
            field=models.IntegerField(default=0, verbose_name='Number of available bikes'),
            preserve_default=False,
        ),
    ]
