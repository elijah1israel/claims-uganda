# Generated by Django 5.1.3 on 2025-01-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0002_notification_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='button_text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
