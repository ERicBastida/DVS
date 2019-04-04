from django.db import models
from django.core.validators import  FileExtensionValidator
from django.urls import reverse

# @TODO: Fix all this, using POO and Desing Patterns
# # # New Code
# class Files:
#     """
#     Abstract class that contains all generics parameter to heredity to subclass
#     """
#     # Determine is a file es input file or output file
#     TYPE_FILE_INPUT = True
#     # This number identifies which function number belongs to
#     FUNCTION_NUMBER = 1
#
#     ROOT_PATH_FILE = 'image/'
#
#     EXTENSION_VALIDATOR = ['BMP', 'PNG', 'PAR', 'TIFF', 'MP4', 'AVI', 'MOV', 'WMV']
#
#     def Files(self,is_input=True,function_number=1):
#         self.TYPE_FILE_INPUT=is_input
#         self.FUNCTION_NUMBER= function_number


# Old code
# Create your models here.
class Files(models.Model):
    image_formats = ["png", "tiff", "bmp"]
    video_formats = ["ogg", "webm", "mp4", "wmv", "avi"]

    imagen = models.FileField(upload_to='images/imagenes/', validators=[
        FileExtensionValidator(['BMP', 'PNG', 'PAR', 'TIFF', 'MP4', 'OGG', 'WEBM', 'MP4'],
                               'The image was not uploaded:invalid format')],
                              help_text='Introduce only format images .png , .tif ,.tiff , .bmp , .webm , .ogg , .mp4 ',
                              verbose_name='file', )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name = string.split('.')[0]
        return name

    def is_image(self):
        result = False
        if self.extension() in self.image_formats:
            result = True
        return result

    def is_video(self):
        result = False
        if self.extension() in self.video_formats:
            result = True
        return result

    def extension(self):
        string = str(self.imagen)
        name = string.split('.')[1]
        return name

    def delete(self, *args, **kwargs):

        self.imagen.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class Files2(models.Model):
    imagen2 = models.FileField(upload_to='images/imagenes2/', validators=[
        FileExtensionValidator(['BMP', 'PNG', 'PAR', 'TIFF', 'MP4', 'AVI', 'MOV', 'WMV'],
                               'The image was not uploaded:invalid format')],
                               help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ',
                               verbose_name='file2', )
    timestamp2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen2)
        name2 = string.split('.')[0]
        return name2

    def delete(self, *args, **kwargs):
        self.imagen2.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'File2'
        verbose_name_plural = 'Files2'


class Files3(models.Model):
    imagen3 = models.FileField(upload_to='images/imagenes3/', validators=[
        FileExtensionValidator(['BMP', 'PNG', 'PAR', 'TIFF', 'MP4', 'AVI', 'MOV', 'WMV'],
                               'The image was not uploaded:invalid format')],
                               help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ',
                               verbose_name='file3', )
    timestamp3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen3)
        name3 = string.split('.')[0]
        return name3

    def delete(self, *args, **kwargs):
        self.imagen3.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'File3'
        verbose_name_plural = 'Files3'


class FilesOutput(models.Model):


    imagenOutput = models.FileField(upload_to='images/imagenes/image-output/',  verbose_name='fileOutput', )
    timestamp = models.DateTimeField(auto_now_add=True)
    in_file_1 = models.IntegerField(verbose_name='first_file',default=0)
    path_file_1 = models.CharField(default="",max_length=100)
    in_file_2 = models.IntegerField(verbose_name='second_file',default=0)
    path_file_2 = models.CharField(default="",max_length=100)

    def __str__(self):
        string = str(self.imagenOutput)
        name = string.split('.')[0]
        return name

    def is_image(self):
        result = False
        if self.extension() in self.image_formats:
            result = True
        return result

    def is_video(self):
        result = False
        if self.extension() in self.video_formats:
            result = True
        return result

    def extension(self):
        string = str(self.imagenOutput)
        name = string.split('.')[1]
        return name

    def delete(self, *args, **kwargs):

        self.imagenOutput.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'FileOutput'
        verbose_name_plural = 'FilesOutput'


class FilesOutput2(models.Model):
    imagenOutput2 = models.FileField(upload_to='images/imagenes2/image-output', validators=[
        FileExtensionValidator(['BMP', 'PNG', 'TIF', 'TIFF', 'MP4', 'AVI', 'MOV', 'WMV'],
                               'The image was not uploaded:invalid format')],
                               help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ',
                               verbose_name='fileOutput2', )
    timestamp2 = models.DateTimeField(auto_now_add=True)
    in_file_1 = models.IntegerField(verbose_name='first_file',default=0)
    path_file_1 = models.CharField(default="",max_length=100)
    in_file_2 = models.IntegerField(verbose_name='second_file',default=0)
    path_file_2 = models.CharField(default="",max_length=100)

    def __str__(self):
        string = str(self.imagenOutput2)
        name2 = string.split('.')[0]
        return name2

    def delete(self, *args, **kwargs):
        self.imagenOutput2.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'FileOutput2'
        verbose_name_plural = 'FilesOutput2'


class FilesOutput3(models.Model):
    imagenOutput3 = models.FileField(upload_to='images/imagenes3/image-output/', validators=[
        FileExtensionValidator(['BMP', 'PNG', 'TIF', 'TIFF', 'MP4', 'AVI', 'MOV', 'WMV'],
                               'The image was not uploaded:invalid format')],
                               help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ',
                               verbose_name='fileOutput3', )
    timestamp3 = models.DateTimeField(auto_now_add=True)

    in_file_1 = models.IntegerField(verbose_name='first_file',default=0)
    path_file_1 = models.CharField(default="",max_length=100)
    in_file_2 = models.IntegerField(verbose_name='second_file',default=0)
    path_file_2 = models.CharField(default="",max_length=100)

    def __str__(self):
        string = str(self.imagenOutput3)
        name3 = string.split('.')[0]
        return name3

    def delete(self, *args, **kwargs):
        self.imagenOutput3.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'FileOutput3'
        verbose_name_plural = 'FilesOutput3'





# Author : Eric Bastida
# Contact: eribastida@gmail.com - Date:
# Date: 23 March 2019


from .views import *


class PreviewFiles(models.Model):
    "Clase encargada de obtener los archivos compatibles para ser previsualizados."

    UNSUPPORT_FORMAT_MESSAGE = "Incompatible Format."
    CONTENT_HTML = ""
    FILE = None
    FILE_ID = 0


    def Files_Preview(self,request,pk):
        self.FILE_ID = pk
        pass

    def view_web_file(self, id):
        "Muestra el archivo en el formato web correspondiente para ser insertado directamente en la pagina"

        try:
            self.FILE = Files.objects.get(pk=id)

            style_image = """
                            position: fixed; 
                            top: 0; 
                            left: 0; 

                            /* Preserve aspet ratio */
                            min-width: 100%;
                            min-height: 100%;
                        """

            name_file = "/media/" + self.FILE.__str__() + "." + self.FILE.extension()

            resultado = "Incompatible Format."

            if self.FILE.is_image() == True:

                resultado = '<img src="' + name_file + '" class="img-responsive" style="' + style_image + '";">'
            elif self.FILE.is_video():
                resultado = '<video   controls   autoplay > <source   src = "' + name_file + '"   type = "video/' + self.FILE.extension() + '" > </source > </video >'

                # resultado = '<head> <link href="https://vjs.zencdn.net/7.4.1/video-js.css" rel="stylesheet"><script src="https://vjs.zencdn.net/ie8/ie8-version/videojs-ie8.min.js"></script></head><body><video  id = "my-video" class ="video-js" controls preload="auto" width="640" height="264"   poster="/media/images/imagenes/datavia_logo.png"   data-setup = "{}">  <source src = "'+name_file+'"  type = "video/'+self.FILE.extension() + '"> <p  class ="vjs-no-js"> To view this video please enable   JavaScript, and consider upgrading to a web browser that <a  href = "https://videojs.com/html5-video-support/"  target = "_blank" > supports HTML5  video </a > </p> </video><script    src = "https://vjs.zencdn.net/7.4.1/video.js" ></script></body >'

        except:

            return None

        return resultado



        