# Generated by Django 2.2.17 on 2020-12-14 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_curso_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
