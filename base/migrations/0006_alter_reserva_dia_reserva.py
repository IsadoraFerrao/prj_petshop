# Generated by Django 4.1.4 on 2023-01-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_reserva_dia_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='dia_reserva',
            field=models.DateTimeField(max_length=14, verbose_name='Dia do Banho'),
        ),
    ]
