# Generated by Django 3.2.20 on 2023-09-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_dates', '0004_auto_20230903_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
