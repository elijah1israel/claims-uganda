# Generated by Django 5.1.3 on 2024-12-13 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cases', '0005_alter_case_policy_alter_case_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='SupportDocuments/files')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cases.case')),
            ],
        ),
    ]