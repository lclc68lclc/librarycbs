# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryinv', '0002_publisher_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('version', models.CharField(max_length=50, null=True, blank=True)),
                ('quantity', models.FloatField()),
                ('title', models.ForeignKey(to='libraryinv.Publication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='lines',
            name='title',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.ForeignKey(to='libraryinv.Line'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Lines',
        ),
    ]
