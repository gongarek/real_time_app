# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_remove_signup_wiadomosc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='czlonkowie',
            name='czlonek',
        ),
        migrations.DeleteModel(
            name='Czlonkowie',
        ),
    ]
