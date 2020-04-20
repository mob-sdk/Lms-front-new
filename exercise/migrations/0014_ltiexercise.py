# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_services', '0004_auto_20150828_1210'),
        ('exercise', '0013_auto_20151222_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='LTIExercise',
            fields=[
                ('baseexercise_ptr', models.OneToOneField(
                    to='exercise.BaseExercise', on_delete=models.CASCADE,
                    auto_created=True, primary_key=True, serialize=False, parent_link=True)),
                ('lti_service', models.ForeignKey(to='external_services.LTIService', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=('exercise.baseexercise',),
        ),
    ]
