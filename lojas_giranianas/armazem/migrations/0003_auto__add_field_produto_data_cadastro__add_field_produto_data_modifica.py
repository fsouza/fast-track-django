# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Produto.data_cadastro'
        db.add_column('armazem_produto', 'data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 1, 15, 22, 42, 52, 515900), blank=True), keep_default=False)

        # Adding field 'Produto.data_modificacao'
        db.add_column('armazem_produto', 'data_modificacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 1, 15, 22, 42, 59, 475953), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Produto.data_cadastro'
        db.delete_column('armazem_produto', 'data_cadastro')

        # Deleting field 'Produto.data_modificacao'
        db.delete_column('armazem_produto', 'data_modificacao')


    models = {
        'armazem.produto': {
            'Meta': {'object_name': 'Produto'},
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_modificacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preco': ('django.db.models.fields.FloatField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['armazem']
