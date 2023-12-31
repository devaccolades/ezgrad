# Generated by Django 4.2.3 on 2023-07-27 06:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0005_coursetype_is_deleted'),
        ('course', '0002_delete_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('university_logo', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('university_name', models.CharField(blank=True, max_length=300, null=True)),
                ('about_university', models.TextField(blank=True, null=True)),
                ('sample_certificate', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('prospectus', models.FileField(blank=True, null=True, upload_to='Files')),
                ('coursetype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.coursetype')),
            ],
            options={
                'db_table': 'University',
            },
        ),
    ]
