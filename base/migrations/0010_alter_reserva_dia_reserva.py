# Generated by Django 4.1.4 on 2023-01-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_reserva_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='dia_reserva',
            field=models.DateTimeField(),
        ),
    ]
