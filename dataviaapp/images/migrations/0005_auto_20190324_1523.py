# Generated by Django 2.1.7 on 2019-03-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_files_preview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files_Preview',
            new_name='PreviewFiles',
        ),
    ]
