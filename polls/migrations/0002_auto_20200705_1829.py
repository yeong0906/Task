# Generated by Django 3.0.7 on 2020-07-05 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='introduction',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='shoe',
            old_name='area',
            new_name='stock',
        ),
    ]
