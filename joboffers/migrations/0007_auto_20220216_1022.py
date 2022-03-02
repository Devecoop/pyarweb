# Generated by Django 3.2.11 on 2022-02-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0006_auto_20220110_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='contact_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL Contacto'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Hora de creación'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Hora de Modificación'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='short_description',
            field=models.TextField(max_length=512, verbose_name='Descripción corta'),
        ),
    ]