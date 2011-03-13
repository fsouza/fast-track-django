# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Categoria.supercategoria'
        db.alter_column('armazem_categoria', 'supercategoria_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['armazem.Categoria']))


    def backwards(self, orm):
        
        # Changing field 'Categoria.supercategoria'
        db.alter_column('armazem_categoria', 'supercategoria_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['armazem.Categoria']))


    models = {
        'armazem.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'supercategoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategorias'", 'null': 'True', 'to': "orm['armazem.Categoria']"})
        },
        'armazem.produto': {
            'Meta': {'object_name': 'Produto'},
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_modificacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preco': ('django.db.models.fields.FloatField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['armazem']
