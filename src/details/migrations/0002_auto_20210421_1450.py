# Generated by Django 3.1 on 2021-04-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cgpa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='student',
            name='credits',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
