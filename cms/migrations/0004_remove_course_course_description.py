# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_course_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_description',
        ),
    ]
