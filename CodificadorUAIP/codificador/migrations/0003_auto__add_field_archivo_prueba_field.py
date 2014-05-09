# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Archivo.prueba_field'
        db.add_column(u'codificador_archivo', 'prueba_field',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Archivo.prueba_field'
        db.delete_column(u'codificador_archivo', 'prueba_field')


    models = {
        u'codificador.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'correlativo_sistema': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'prueba_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Serie']"}),
            'tipo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['codificador.Tipo']"}),
            'unidad_responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Unidad']"})
        },
        u'codificador.archivohistorico': {
            'Meta': {'object_name': 'ArchivoHistorico'},
            'archivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Archivo']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'correlativo_sistema': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
        u'codificador.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'unidad_superior': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Unidad']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['codificador']