# Generated by Django 3.2.9 on 2022-01-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0003_auto_20211125_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='short_description',
            field=models.TextField(default=' ', verbose_name='Descripción corta'),
            preserve_default=False,
        ),
    ]