# Generated by Django 2.0 on 2018-06-30 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180630_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readnum',
            old_name='readed_num',
            new_name='read_num',
        ),
    ]
