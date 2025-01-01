# Generated by Django 5.1.3 on 2024-12-01 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cases', '0001_initial'),
        ('FeeNotes', '0001_initial'),
        ('Pictures', '0001_initial'),
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='fee_note',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_feenote', to='FeeNotes.feenote'),
        ),
        migrations.AddField(
            model_name='case',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='Pictures.picture'),
        ),
        migrations.AddField(
            model_name='case',
            name='reports',
            field=models.ManyToManyField(blank=True, related_name='case_reports', to='Reports.report'),
        ),
    ]