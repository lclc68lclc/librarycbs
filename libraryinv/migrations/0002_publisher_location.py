# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryinv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='location',
            field=models.ForeignKey(default=b'ATL', to='libraryinv.Location'),
            preserve_default=True,
        ),
    ]
