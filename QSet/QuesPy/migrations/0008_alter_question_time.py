# Generated by Django 4.1.1 on 2022-10-02 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuesPy', '0007_alter_question_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 3, 1, 18, 50, 934866)),
        ),
    ]
