# Generated by Django 4.1.4 on 2024-01-26 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0002_exam_management_duration_history_management_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='biil_id',
            new_name='bill_id',
        ),
    ]