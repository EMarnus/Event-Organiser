# Generated by Django 3.2.20 on 2023-09-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_dates', '0002_appointment_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]