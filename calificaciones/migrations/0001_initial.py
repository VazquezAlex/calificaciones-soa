# Generated by Django 3.0.6 on 2020-06-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaCalificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.CharField(max_length=50, verbose_name='Nombre del alumno')),
                ('materia', models.CharField(max_length=50, verbose_name='Materia')),
                ('calificacion1', models.IntegerField(verbose_name='Calificación 1')),
                ('calificacion2', models.IntegerField(verbose_name='Calificación 2')),
                ('calificacion3', models.IntegerField(verbose_name='Calificación 3')),
                ('promedio', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Promedio')),
            ],
        ),
    ]
