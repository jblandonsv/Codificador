# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Empleado'
        db.delete_table(u'codificador_empleado')

        # Adding model 'UnidadesPermitidas'
        db.create_table(u'codificador_unidadespermitidas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('unidades', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Unidad'])),
        ))
        db.send_create_signal(u'codificador', ['UnidadesPermitidas'])


    def backwards(self, orm):
        # Adding model 'Empleado'
        db.create_table(u'codificador_empleado', (
            ('unidades', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Unidad'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'codificador', ['Empleado'])

        # Deleting model 'UnidadesPermitidas'
        db.delete_table(u'codificador_unidadespermitidas')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'codificador.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'codigo_referencia': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'correlativo_sistema': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'fecha_actualizacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Serie']"}),
            'tipo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['codificador.Tipo']"}),
            'unidad_responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Unidad']"}),
            'unidades_bajo_codigo': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'})
        },
        u'codificador.archivohistorico': {
            'Meta': {'object_name': 'ArchivoHistorico'},
            'archivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Archivo']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'reference_descriptivo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'unidad_responsable': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'codificador.correlativo': {
            'Meta': {'object_name': 'Correlativo'},
            'correlativo_actual': ('django.db.models.fields.IntegerField', [], {}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'codificador.dependencia': {
            'Meta': {'object_name': 'Dependencia'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'codificador.estadoexpediente': {
            'Meta': {'object_name': 'EstadoExpediente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'codificador.folio': {
            'Meta': {'object_name': 'folio'},
            'archivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Archivo']"}),
            'cantidad_paginas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'digital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.EstadoExpediente']", 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fisico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'tipo_de_informacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.TipoInformacion']", 'blank': 'True'}),
            'tipo_vigencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.TipoVigencia']", 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'codificador.foliohistorico': {
            'Meta': {'object_name': 'FolioHistorico'},
            'archivo_historico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.ArchivoHistorico']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'tipo_de_informacion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'codificador.serie': {
            'Meta': {'object_name': 'Serie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'codificador.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Serie']"})
        },
        u'codificador.tipoinformacion': {
            'Meta': {'object_name': 'TipoInformacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'codificador.tipovigencia': {
            'Meta': {'object_name': 'TipoVigencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'codificador.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'reference_descriptivo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'unidad_superior': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Unidad']", 'null': 'True', 'blank': 'True'})
        },
        u'codificador.unidadespermitidas': {
            'Meta': {'object_name': 'UnidadesPermitidas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidades': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Unidad']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['codificador']