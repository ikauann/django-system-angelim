# Generated by Django 4.0.1 on 2022-02-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bling', '0003_alter_blingestoque_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='blingestoque',
            name='codigo',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blingestoque',
            name='preco',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blingestoque',
            name='produto',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
