# Generated by Django 2.2.17 on 2020-12-03 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('noCarnet', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField()),
                ('noCarnet', models.CharField(max_length=10)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GradoEst', to='registro.Grado')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sección', to='registro.Seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Docente', to='registro.Docente')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Grado', to='registro.Grado')),
            ],
        ),
    ]
