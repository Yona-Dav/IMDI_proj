# Generated by Django 3.2.9 on 2021-11-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_auto_20211201_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingfilm',
            name='rating',
            field=models.CharField(choices=[('*', '*'), ('**', '**')], max_length=100),
        ),
    ]
