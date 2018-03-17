# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=30, db_tablespace='CEDULA')),
                ('nombres', models.CharField(max_length=70, db_tablespace='NOMBRES')),
                ('apellido', models.CharField(max_length=70, db_tablespace='APELLIDOS')),
                ('codigo', models.CharField(max_length=100, db_tablespace='CODIGO')),
                ('aprobo', models.CharField(max_length=70, db_tablespace='APROBO')),
                ('fecha', models.DateTimeField(db_tablespace='fecha')),
                ('horas', models.CharField(max_length=3, db_tablespace='HORAS')),
            ],
            options={
                'db_table': 'certificaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=30, db_tablespace='USUARIO')),
                ('clave', models.CharField(max_length=30, db_tablespace='CLAVE')),
            ],
            options={
                'db_table': 'usuarios',
            },
            bases=(models.Model,),
        ),
    ]
