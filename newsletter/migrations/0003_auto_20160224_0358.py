# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20160224_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singup',
            old_name='tiemstamp',
            new_name='timestamp',
        ),
    ]
