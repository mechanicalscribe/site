# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'site_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'site', ['Member'])

        # Adding model 'Sticky'
        db.create_table(u'site_sticky', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('description_markdown', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'site', ['Sticky'])

        # Adding model 'Homepage'
        db.create_table(u'site_homepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'site', ['Homepage'])

        # Adding model 'ActiveHomepage'
        db.create_table(u'site_activehomepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active_page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site.Homepage'])),
        ))
        db.send_create_signal(u'site', ['ActiveHomepage'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'site_member')

        # Deleting model 'Sticky'
        db.delete_table(u'site_sticky')

        # Deleting model 'Homepage'
        db.delete_table(u'site_homepage')

        # Deleting model 'ActiveHomepage'
        db.delete_table(u'site_activehomepage')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_markdown': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        }
    }

    complete_apps = ['site']