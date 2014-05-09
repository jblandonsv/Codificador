# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FolioHistorico'
        db.create_table(u'codificador_foliohistorico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archivo_historico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.ArchivoHistorico'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('tipo_de_informacion', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=600, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'codificador', ['FolioHistorico'])


    def backwards(self, orm):
        # Deleting model 'FolioHistorico'
        db.delete_table(u'codificador_foliohistorico')


    models = {
        u'codificador.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'codigo_referencia': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'correlativo_sistema': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Dependencia']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'digital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_actualizacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fisico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'codificador.folio': {
            'Meta': {'object_name': 'folio'},
            'archivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.Archivo']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'tipo_de_informacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['codificador.TipoInformacion']", 'blank': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
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
        }
    }

    complete_apps = ['codificador']