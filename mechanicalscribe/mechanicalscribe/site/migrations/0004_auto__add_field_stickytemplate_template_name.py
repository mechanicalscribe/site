# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StickyTemplate.template_name'
        db.add_column(u'site_stickytemplate', 'template_name',
                      self.gf('django.db.models.fields.CharField')(default='list.html', max_length=18),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StickyTemplate.template_name'
        db.delete_column(u'site_stickytemplate', 'template_name')


    models = {
        u'site.activehomepage': {
            'Meta': {'object_name': 'ActiveHomepage'},
            'active_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.Homepage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'site.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'code': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'site.member': {
            'Meta': {'object_name': 'Member'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        u'site.sticky': {
            'Meta': {'object_name': 'Sticky'},
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_markdown': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.StickyTemplate']", 'null': 'True', 'blank': 'True'})
        },
        u'site.stickytemplate': {
            'Meta': {'object_name': 'StickyTemplate'},
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_markdown': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "'list.html'", 'max_length': '18'})
        }
    }

    complete_apps = ['site']