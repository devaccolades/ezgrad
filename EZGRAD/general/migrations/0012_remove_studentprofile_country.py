# Generated by Django 4.2.3 on 2023-08-17 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_alter_studentprofile_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='country',
        ),
    ]