# Generated by Django 4.1.7 on 2023-03-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_event_delete_customer_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.CharField(max_length=255),
        ),
    ]