# Generated by Django 4.1.4 on 2024-01-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abnormal_behavior', '0003_rename_biil_id_bill_bill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
