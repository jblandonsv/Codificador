# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dependencia'
        db.create_table(u'codificador_dependencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefijo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'codificador', ['Dependencia'])

        # Adding model 'Correlativo'
        db.create_table(u'codificador_correlativo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Dependencia'])),
            ('correlativo_actual', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'codificador', ['Correlativo'])

        # Adding model 'Unidad'
        db.create_table(u'codificador_unidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefijo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Dependencia'])),
            ('unidad_superior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Unidad'], null=True, blank=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'codificador', ['Unidad'])

        # Adding model 'Serie'
        db.create_table(u'codificador_serie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefijo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'codificador', ['Serie'])

        # Adding model 'Tipo'
        db.create_table(u'codificador_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefijo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Serie'])),
        ))
        db.send_create_signal(u'codificador', ['Tipo'])

        # Adding model 'Archivo'
        db.create_table(u'codificador_archivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Dependencia'])),
            ('unidad_responsable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Unidad'])),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Serie'])),
            ('tipo', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['codificador.Tipo'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=600, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('correlativo_sistema', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('prueba_field', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'codificador', ['Archivo'])

        # Adding model 'ArchivoHistorico'
        db.create_table(u'codificador_archivohistorico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codificador.Archivo'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('dependencia', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('unidad_responsable', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('serie', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=600, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('correlativo_sistema', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'codificador', ['ArchivoHistorico'])


    def backwards(self, orm):
        # Deleting model 'Dependencia'
        db.delete_table(u'codificador_dependencia')

        # Deleting model 'Correlativo'
        db.delete_table(u'codificador_correlativo')

        # Deleting model 'Unidad'
        db.delete_table(u'codificador_unidad')

        # Deleting model 'Serie'
        db.delete_table(u'codificador_serie')

        # Deleting model 'Tipo'
        db.delete_table(u'codificador_tipo')

        # Deleting model 'Archivo'
        db.delete_table(u'codificador_archivo')

        # Deleting model 'ArchivoHistorico'
        db.delete_table(u'codificador_archivohistorico')


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