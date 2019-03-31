from django.db import models
from django.core.validators import  FileExtensionValidator
from django.urls import reverse
# Create your models here.
class Files(models.Model):
    
    
    imagen = models.FileField(upload_to='images/imagenes/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file',)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name = string.split('.')[0]
        return name

    def delete(self, *args, **kwargs):
    
        self.imagen.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'



class Files2(models.Model):


    imagen2 = models.FileField(upload_to='images/imagenes2/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file2',)
    timestamp2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name2 = string.split('.')[0]
        return name2

    def delete(self, *args, **kwargs):
        
        self.imagen2.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File2'
        verbose_name_plural = 'Files2'


class Files3(models.Model):


    imagen3 = models.FileField(upload_to='images/imagenes3/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file3',)
    timestamp3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name3 = string.split('.')[0]
        return name3

    def delete(self, *args, **kwargs):
        
        self.imagen3.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File3'
        verbose_name_plural = 'Files3'

        