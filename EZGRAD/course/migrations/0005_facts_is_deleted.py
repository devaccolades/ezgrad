# Generated by Django 4.2.3 on 2023-07-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_facts'),
    ]

    operations = [
        migrations.AddField(
            model_name='facts',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]