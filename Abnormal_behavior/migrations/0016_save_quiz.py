# Generated by Django 4.2.4 on 2024-03-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0015_quiz_delete_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.CharField(max_length=100)),
                ('json_data', models.JSONField()),
            ],
        ),
    ]
