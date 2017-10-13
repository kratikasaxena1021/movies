# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_remove_course_course_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_instructor',
            new_name='course_tutor',
        ),
    ]
