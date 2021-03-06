# Generated by Django 2.1.7 on 2019-03-24 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20190318_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='imagen',
            field=models.FileField(help_text='Introduce only format images .png , .tif ,.tiff , .bmp , .webm , .ogg , .mp4 ', upload_to='images/imagenes/', validators=[django.core.validators.FileExtensionValidator(['BMP', 'PNG', 'TIF', 'TIFF', 'MP4', 'OGG', 'WEBM', 'MP4'], 'The image was not uploaded:invalid format')], verbose_name='file'),
        ),
    ]
