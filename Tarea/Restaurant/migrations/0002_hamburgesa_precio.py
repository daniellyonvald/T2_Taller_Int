# Generated by Django 3.0.5 on 2020-05-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburgesa',
            name='precio',
            field=models.IntegerField(default=7),
        ),
    ]
