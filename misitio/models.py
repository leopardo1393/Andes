# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class usuarios(models.Model):
	usuario = models.CharField(max_length=30, db_tablespace= "USUARIO")
	clave = models.CharField(max_length=30, db_tablespace= "CLAVE")
	class Meta:
		db_table ='usuarios'
	def __unicode__(self):
		return self.usuario	

class certificaciones(models.Model):
	cedula = models.CharField(max_length=30, db_tablespace= "CEDULA")
	nombres = models.CharField(max_length=70, db_tablespace= "NOMBRES")
	apellido = models.CharField(max_length=70, db_tablespace= "APELLIDOS")
	codigo = models.CharField(max_length=100, db_tablespace= "CODIGO")
	aprobo = models.CharField(max_length=70, db_tablespace= "APROBO")
	fecha = models.DateTimeField(db_tablespace= "fecha")
	horas = models.CharField(max_length=3, db_tablespace= "HORAS")
	class Meta:
		db_table = 'certificaciones'
	def __unicode__(self):
		return self.cedula
		