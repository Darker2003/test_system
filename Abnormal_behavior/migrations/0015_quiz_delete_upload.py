# Generated by Django 4.2.9 on 2024-03-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0014_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
                ('json_data', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
