# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RequestNotification'
        db.delete_table(u'projects_requestnotification')

        # Deleting model 'Request'
        db.delete_table(u'projects_request')

        # Adding model 'HelpOffer'
        db.create_table(u'projects_helpoffer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=10)),
        ))
        db.send_create_signal(u'projects', ['HelpOffer'])

        # Adding model 'Notification'
        db.create_table(u'projects_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('help_offer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.HelpOffer'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_sender', to=orm['users.UserProfile'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_receiver', to=orm['users.UserProfile'])),
            ('seen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Notification'])


    def backwards(self, orm):
        # Adding model 'RequestNotification'
        db.create_table(u'projects_requestnotification', (
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_sender', to=orm['users.UserProfile'])),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Request'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_receiver', to=orm['users.UserProfile'])),
            ('seen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'projects', ['RequestNotification'])

        # Adding model 'Request'
        db.create_table(u'projects_request', (
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=10)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'projects', ['Request'])

        # Deleting model 'HelpOffer'
        db.delete_table(u'projects_helpoffer')

        # Deleting model 'Notification'
        db.delete_table(u'projects_notification')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.helpoffer': {
            'Meta': {'object_name': 'HelpOffer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '10'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'projects.notification': {
            'Meta': {'object_name': 'Notification'},
            'help_offer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.HelpOffer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'noti_receiver'", 'to': u"orm['users.UserProfile']"}),
            'seen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'noti_sender'", 'to': u"orm['users.UserProfile']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_charity'", 'to': u"orm['users.UserProfile']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'developers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'project_developers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['users.UserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'need_locals': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.Skill']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.State']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'looking'", 'max_length': '50'}),
            'time_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'users.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'allow_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['users.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['users.Skill']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['users.State']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'www': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']