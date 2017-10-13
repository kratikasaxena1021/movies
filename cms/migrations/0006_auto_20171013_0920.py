# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20171013_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_tutor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
