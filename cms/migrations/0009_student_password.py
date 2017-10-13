# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
