# Generated by Django 2.1.2 on 2020-04-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='stock_id',
            field=models.CharField(max_length=200, verbose_name='股票id'),
        ),
    ]
