# Generated by Django 2.2.3 on 2019-10-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0002_user_is_hr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_intern',
            field=models.BooleanField(default=False),
        ),
    ]
