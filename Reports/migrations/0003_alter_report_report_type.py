# Generated by Django 5.1.3 on 2024-12-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_report_submissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('Preliminary', 'Preliminary'), ('Addendum', 'Addendum'), ('Final', 'Final')], default='Not Selected', max_length=50),
        ),
    ]
