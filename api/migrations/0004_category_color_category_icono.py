# Generated by Django 5.0.7 on 2024-08-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_transaction_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default='#FFDE59', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='icono',
            field=models.CharField(default='clipboard-plus-svgrepo-com', max_length=50),
            preserve_default=False,
        ),
    ]
