# Generated by Django 4.1.1 on 2022-10-02 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuesPy', '0003_alter_question_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 2, 16, 15, 19, 560218)),
        ),
    ]
