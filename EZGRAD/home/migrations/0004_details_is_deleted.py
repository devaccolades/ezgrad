# Generated by Django 4.2.3 on 2023-07-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]