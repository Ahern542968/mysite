# Generated by Django 2.0 on 2018-08-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_parent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
    ]
