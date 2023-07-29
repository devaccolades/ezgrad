# Generated by Django 4.2.3 on 2023-07-29 09:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facts', models.TextField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.university')),
            ],
            options={
                'db_table': 'Facts',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('duration_description', models.TextField(blank=True, null=True)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('course_details', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='Files')),
                ('audio', models.FileField(blank=True, null=True, upload_to='Files')),
                ('eligibility', models.CharField(blank=True, max_length=200, null=True)),
                ('eligibility_description', models.TextField(blank=True, null=True)),
                ('admission_procedure', models.FileField(blank=True, null=True, upload_to='Files')),
                ('fees', models.CharField(blank=True, max_length=300, null=True)),
                ('fees_description', models.TextField(blank=True, null=True)),
                ('syllabus', models.FileField(blank=True, null=True, upload_to='Files')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.university')),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_by', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('is_deleted', models.BooleanField(default=False)),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.university')),
            ],
            options={
                'db_table': 'Approval',
            },
        ),
    ]