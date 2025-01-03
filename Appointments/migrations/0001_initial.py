# Generated by Django 5.1.3 on 2024-12-08 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.EmailField(max_length=254)),
                ('person_contact', models.CharField(max_length=20)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.staff')),
            ],
        ),
    ]
