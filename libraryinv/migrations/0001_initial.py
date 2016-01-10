# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_number', models.CharField(max_length=150)),
                ('tax', models.FloatField()),
                ('shipping', models.FloatField()),
                ('total', models.FloatField()),
                ('date_purchased', models.DateField()),
                ('order_type', models.CharField(max_length=50)),
                ('date_sent_acctg', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('version', models.CharField(max_length=50, null=True, blank=True)),
                ('quantity', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(default=b'ATL', max_length=3, choices=[(b'ASH', b'Asheville'), (b'ATL', b'Atlanta'), (b'AUS', b'Austin'), (b'BHM', b'Birmingham'), (b'BOS', b'Boston'), (b'COL', b'Columbia'), (b'DAL', b'Dallas'), (b'DEN', b'Denver'), (b'ENC', b'Encino'), (b'FAR', b'Fairfax'), (b'GRE', b'Greenville'), (b'JAC', b'Jacksonville'), (b'KAS', b'Kansas City'), (b'MAC', b'Macon'), (b'MAD', b'Madison'), (b'NAS', b'Nashville'), (b'NYC', b'New York'), (b'OPE', b'Opelika'), (b'PRI', b'Princeton'), (b'STL', b'St. Louis'), (b'TAM', b'Tampa'), (b'WSA', b'Winston-Salem')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publication_title', models.CharField(max_length=200, null=True, blank=True)),
                ('publication_number', models.CharField(max_length=50, null=True, blank=True)),
                ('publication_type', models.CharField(default=b'S', max_length=2, choices=[(b'B', b'Book'), (b'S', b'Subscription')])),
                ('price', models.FloatField()),
                ('location', models.ForeignKey(to='libraryinv.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher', models.CharField(max_length=150, unique=True, serialize=False, primary_key=True)),
                ('account_number', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lines',
            name='title',
            field=models.ForeignKey(to='libraryinv.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.ForeignKey(to='libraryinv.Lines'),
            preserve_default=True,
        ),
    ]
