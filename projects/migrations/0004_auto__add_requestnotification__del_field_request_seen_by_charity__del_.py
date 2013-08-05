# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestNotification'
        db.create_table(u'projects_requestnotification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Request'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_sender', to=orm['users.UserProfile'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noti_receiver', to=orm['users.UserProfile'])),
            ('seen', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'projects', ['RequestNotification'])

        # Deleting field 'Request.seen_by_charity'
        db.delete_column(u'projects_request', 'seen_by_charity')

        # Deleting field 'Request.time_accepted'
        db.delete_column(u'projects_request', 'time_accepted')

        # Adding field 'Request.status'
        db.add_column(u'projects_request', 'status',
                      self.gf('django.db.models.fields.CharField')(default='pending', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'RequestNotification'
        db.delete_table(u'projects_requestnotification')

        # Adding field 'Request.seen_by_charity'
        db.add_column(u'projects_request', 'seen_by_charity',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Request.time_accepted'
        db.add_column(u'projects_request', 'time_accepted',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Request.status'
        db.delete_column(u'projects_request', 'status')


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
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_charity'", 'to': u"orm['users.UserProfile']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'developers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'project_developers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['users.UserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'need_locals': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.Skill']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.State']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'projects.request': {
            'Meta': {'object_name': 'Request'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '10'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'projects.requestnotification': {
            'Meta': {'object_name': 'RequestNotification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'noti_receiver'", 'to': u"orm['users.UserProfile']"}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Request']"}),
            'seen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'noti_sender'", 'to': u"orm['users.UserProfile']"})
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
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['users.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.Skill']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['users.State']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['projects']