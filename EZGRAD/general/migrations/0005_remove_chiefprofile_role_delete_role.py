# Generated by Django 4.2.3 on 2023-08-01 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_role_chiefprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chiefprofile',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]