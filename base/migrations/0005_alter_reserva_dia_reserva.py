# Generated by Django 4.1.4 on 2023-01-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_contato_options_alter_reserva_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='dia_reserva',
            field=models.DateField(max_length=14, verbose_name='Dia do Banho'),
        ),
    ]
