# Generated by Django 5.1 on 2024-08-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_report_transaction_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(),
        ),
    ]