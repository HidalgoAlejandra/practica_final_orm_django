# Generated by Django 4.1.1 on 2023-07-30 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='f_fabricacion',
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
    ]
