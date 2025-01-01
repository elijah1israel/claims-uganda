# Generated by Django 5.1.3 on 2024-12-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeNotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feenote',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid', max_length=50),
        ),
    ]