# Generated by Django 5.1.3 on 2024-12-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='caption',
            field=models.CharField(max_length=50, null=True),
        ),
    ]