# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20170213_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='wiadomosc',
        ),
    ]
