# Generated by Django 2.0 on 2020-11-28 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201127_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogarticle',
            name='author',
        ),
    ]
