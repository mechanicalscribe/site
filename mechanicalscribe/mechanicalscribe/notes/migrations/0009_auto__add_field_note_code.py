# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Note.code'
        db.add_column(u'notes_note', 'code',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Note.code'
        db.delete_column(u'notes_note', 'code')


    models = {
        u'notes.note': {
            'Meta': {'object_name': 'Note'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.Member']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_markdown': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'homepage_priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'homepage_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'stickies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['site.Sticky']", 'null': 'True', 'symmetrical': 'False'}),
            'stills': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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

    complete_apps = ['notes']