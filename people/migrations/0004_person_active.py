# Generated by Django 2.0.2 on 2018-03-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
