# Generated by Django 2.2.3 on 2020-01-04 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20200104_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='diagram_name',
            new_name='diagram',
        ),
    ]
