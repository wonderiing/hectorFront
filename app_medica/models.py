# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Citas(models.Model):
    id_cita = models.AutoField(db_column='ID_Cita', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='ID_Paciente', blank=True, null=True)  # Field name made lowercase.
    id_medico = models.ForeignKey('Medicos', models.DO_NOTHING, db_column='ID_Medico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citas'


class Consultas(models.Model):
    id_consulta = models.AutoField(db_column='ID_Consulta', primary_key=True)  # Field name made lowercase.
    id_cita = models.ForeignKey(Citas, models.DO_NOTHING, db_column='ID_Cita', blank=True, null=True)  # Field name made lowercase.
    notas = models.TextField(db_column='Notas', blank=True, null=True)  # Field name made lowercase.
    diagnóstico = models.TextField(db_column='Diagnóstico', blank=True, null=True)  # Field name made lowercase.
    tratamiento = models.TextField(db_column='Tratamiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultas'


class Medicos(models.Model):
    id_medico = models.AutoField(db_column='ID_Medico', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicos'


class Pacientes(models.Model):
    id_paciente = models.AutoField(db_column='ID_Paciente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=True, null=True)  # Field name made lowercase.
    teléfono = models.CharField(db_column='Teléfono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    correo_electrónico = models.CharField(db_column='Correo_Electrónico', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pacientes'
