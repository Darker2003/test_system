# Generated by Django 4.1.4 on 2024-02-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0007_history_management_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(db_index=True, max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam_management',
            name='course_id',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='exam_management',
            name='exam_id',
            field=models.CharField(db_index=True, max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam_room_doing',
            name='erd_id',
            field=models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='history_management',
            name='his_id',
            field=models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_management',
            name='username',
            field=models.CharField(db_index=True, max_length=15, primary_key=True, serialize=False),
        ),
    ]
