# Generated by Django 5.1.3 on 2025-01-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeNotes', '0004_feenote_last_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='feenote',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('UGX', 'UGX')], default='USD', max_length=50),
        ),
    ]
