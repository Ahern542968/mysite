# Generated by Django 2.0 on 2018-08-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_remove_comment_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
