# Generated by Django 3.2.11 on 2022-04-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0011_auto_20220405_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffervisualization',
            name='event_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Visualización en Listado'), (1, 'Visualización de la oferta completa'), (2, 'Apertura de la información de contacto')], verbose_name='Tipo de Evento'),
        ),
    ]