# Generated by Django 3.0.2 on 2020-02-09 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websocket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connection',
            old_name='conection_id',
            new_name='connection_id',
        ),
    ]
