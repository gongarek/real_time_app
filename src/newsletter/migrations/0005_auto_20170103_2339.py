# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_signup_akceptacja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='akceptacja',
            field=models.BooleanField(),
        ),
    ]
