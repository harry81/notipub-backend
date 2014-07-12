# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeviceToken'
        db.create_table(u'notipub_message_devicetoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.TextField')(default='')),
            ('uuid', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'notipub_message', ['DeviceToken'])


    def backwards(self, orm):
        # Deleting model 'DeviceToken'
        db.delete_table(u'notipub_message_devicetoken')


    models = {
        u'notipub_message.devicetoken': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'DeviceToken'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'token': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'uuid': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'})
        }
    }

    complete_apps = ['notipub_message']