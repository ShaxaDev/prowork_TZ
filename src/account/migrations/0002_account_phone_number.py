# Generated by Django 3.2 on 2021-07-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='993328405', max_length=25),
        ),
    ]
