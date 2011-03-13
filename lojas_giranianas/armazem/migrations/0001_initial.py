# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Produto'
        db.create_table('armazem_produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('preco', self.gf('django.db.models.fields.FloatField')()),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('armazem', ['Produto'])


    def backwards(self, orm):
        
        # Deleting model 'Produto'
        db.delete_table('armazem_produto')


    models = {
        'armazem.produto': {
            'Meta': {'object_name': 'Produto'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preco': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['armazem']
