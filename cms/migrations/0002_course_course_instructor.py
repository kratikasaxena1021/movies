# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_instructor',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
