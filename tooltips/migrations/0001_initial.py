# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependences = []

    operations = [
        migrations.CreateModel(
            name='Tooltip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=255, db_index=True)),
                ('selector', models.CharField(max_length=50, default='', blank=False, null=False, help_text='div:contains("example")')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            bases=(models.Model,),
        )
    ]
