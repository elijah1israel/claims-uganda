# Generated by Django 5.1.3 on 2025-01-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]