from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from .FilesProcessor import *

from django.core.files.base import File


class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class PreviewFiles(CreateView):
    "Clase encargada de mostrar la vista previsualizadora de contenido."

    template_name = 'preview.html'

    def get_context_data(self, **kwargs):
        context = super(PreviewFiles, self).get_context_data(**kwargs)
        context['file_to_preview'] = True

        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class UploadFileView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy('files_list')
    template_name = 'upload_file.html'
    
    def get_context_data(self, **kwargs):
        context = super(UploadFileView, self).get_context_data(**kwargs)
        context['Files'] = Files.objects.all()
        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()


        return self.render_to_response(self.get_context_data(form=form))

class UploadFileView2(CreateView):
    model = Files2
    form_class = FilesForm2
    success_url = reverse_lazy('files_list2')
    template_name = 'upload_file2.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(UploadFileView2, self).get_context_data(**kwargs)
        context['Files2'] = Files2.objects.all()
        return context
    

    def form_invalid(self, form):
        
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

class UploadFileView3(CreateView):
    model = Files3
    form_class = FilesForm3
    success_url = reverse_lazy('files_list3')
    template_name = 'upload_file3.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(UploadFileView3, self).get_context_data(**kwargs)
        context['Files3'] = Files3.objects.all()
        return context
    

    def form_invalid(self, form):
        
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

class OutputFileView(CreateView):
    model = FilesOutput
    form_class = FilesOutputForm
    success_url = reverse_lazy('files_list')
    template_name = 'output_file.html'


    def get_context_data(self, **kwargs):
        context = super(OutputFileView, self).get_context_data(**kwargs)
        context['FilesOutput'] = FilesOutput.objects.all()

        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

class OutputFileView2(CreateView):
    model = FilesOutput2
    form_class = FilesForm2
    success_url = reverse_lazy('files_list2')
    template_name = 'output_file2.html'

    def get_context_data(self, **kwargs):
        context = super(OutputFileView2, self).get_context_data(**kwargs)
        context['FilesOutput2'] = FilesOutput2.objects.all()
        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

class OutputFileView3(CreateView):
    model = FilesOutput3
    form_class = FilesOutputForm3
    success_url = reverse_lazy('files_list3')
    template_name = 'output_file3.html'

    def get_context_data(self, **kwargs):
        context = super(OutputFileView3, self).get_context_data(**kwargs)
        context['FilesOutput3'] = FilesOutput3.objects.all()
        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

def delete_file(request, pk):
    if request.method == 'POST':
        file = Files.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file')

def delete_file2(request, pk):
    if request.method == 'POST':
        file = Files2.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file2')

def delete_file3(request, pk):
    if request.method == 'POST':
        file = Files3.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file3')

def delete_file_output(request, pk):
    if request.method == 'POST':
        file = FilesOutput.objects.get(pk=pk)
        file.delete()
    return redirect('class_output_file')

def delete_file2_output(request, pk):
    if request.method == 'POST':
        file = FilesOutput2.objects.get(pk=pk)
        file.delete()
    return redirect('class_output_file2')

def delete_file3_output(request, pk):
    if request.method == 'POST':
        file = FilesOutput3.objects.get(pk=pk)
        file.delete()
    return redirect('class_output_file3')


def process_file(request):
    # try:
    print("------>Data receiver from JavaScript : ",request)

    function_number = request.GET.get('function_number', None)
    file1_pk = request.GET.get('file1_pk', None)
    file2_pk = request.GET.get('file2_pk', None)



    # @TODO: Fix model (read TODO description there)
    # It not good code


    if (function_number == "1" ):

        file1 = Files.objects.get(pk=file1_pk)
        file2 = Files.objects.get(pk=file2_pk)
        file1_path = file1.imagen.url
        file2_path = file2.imagen.url

    elif (function_number == "2"):
        file1 = Files2.objects.get(pk=file1_pk)
        file2 = Files2.objects.get(pk=file2_pk)
        file1_path = file1.imagen2.url
        file2_path = file2.imagen2.url

    elif (function_number == "3"):
        file1 = Files3.objects.get(pk=file1_pk)
        file2 = Files3.objects.get(pk=file2_pk)
        file1_path = file1.imagen3.url
        file2_path = file2.imagen3.url
    else:
         JsonResponse({'status':'false','message':"Number funcion incorrect" + function_number}, status=500)


    # Aca se envia los dos nombres de archivo para ser procesados por la placa
    files_to_process = FileProcessor()

    result = files_to_process.work(function_number, file1_path,file2_path)



    try:
        if (function_number == "1"):
            file = FilesOutput()
            file.imagenOutput = File(open(result, "rb"))

        elif (function_number == "2"):
            file = FilesOutput2()
            file.imagenOutput2 = File(open(result, "rb"))
        else:
            file = FilesOutput3()
            file.imagenOutput3 = File(open(result, "rb"))
            # file.imagenOutput3 =File(open(result, "rb"))


        file.in_file_1 = file1_pk
        file.path_file_1 = file1_path
        file.in_file_2 = file2_pk
        file.path_file_2 = file2_path
        file.save()

    except FileNotFoundError :
        JsonResponse({'status': 'false', 'message': "File result not found." }, status=403)



    # Crear objeto del tipo que sea y asignarle los dos archivos

    # except:
    #     import sys
    #     # @TODO: Implementing  tracker error system and return result
    #     print("Oops!", sys.exc_info(), "occured.")
    #     JsonResponse({'status': 'false', 'message': "Error."}, status=403)


    return JsonResponse({"events": result})





