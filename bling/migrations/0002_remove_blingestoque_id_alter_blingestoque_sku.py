# Generated by Django 4.0.1 on 2022-01-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blingestoque',
            name='id',
        ),
        migrations.AlterField(
            model_name='blingestoque',
            name='sku',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
