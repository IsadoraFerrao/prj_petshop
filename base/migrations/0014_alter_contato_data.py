# Generated by Django 4.1.4 on 2023-01-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_reserva_dia_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Envio'),
        ),
    ]
