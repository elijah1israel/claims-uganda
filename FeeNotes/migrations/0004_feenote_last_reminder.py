# Generated by Django 5.1.3 on 2024-12-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeNotes', '0003_feenote_valid_fee_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='feenote',
            name='last_reminder',
            field=models.DateTimeField(null=True),
        ),
    ]