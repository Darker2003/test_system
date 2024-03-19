# Generated by Django 4.2.9 on 2024-03-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0013_merge_20240305_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload')),
                ('json_data', models.JSONField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]