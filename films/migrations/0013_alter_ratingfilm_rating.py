# Generated by Django 3.2.9 on 2021-11-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_alter_ratingfilm_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingfilm',
            name='rating',
            field=models.CharField(choices=[('*', '*'), ('* *', '* *'), ('* * *', '* * *'), ('* * * *', '* * * *'), ('* * * * *', '* * * * *')], max_length=100),
        ),
    ]
