# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20171013_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_lang',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
    ]
