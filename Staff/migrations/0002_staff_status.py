# Generated by Django 5.1.3 on 2024-12-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=100),
        ),
    ]