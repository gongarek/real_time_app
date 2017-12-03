# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20170103_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='akceptacja',
            field=models.BooleanField(default=None),
        ),
    ]
