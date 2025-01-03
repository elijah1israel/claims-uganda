# Generated by Django 5.1.3 on 2024-12-01 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Assessors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_Company', models.CharField(choices=[('Jubilee', 'Jubilee')], default='Not Selected', max_length=50)),
                ('policy', models.CharField(choices=[('Jubilee', 'Jubilee')], default='Not Selected', max_length=50)),
                ('date_reported', models.DateField()),
                ('client', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('reference_number', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], default='Not Selected', max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('assessor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='_case_assessor', to='Assessors.assessor')),
            ],
        ),
    ]
