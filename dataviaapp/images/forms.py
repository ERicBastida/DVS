from django import forms
from .models import *

# @TODO: Using hierarchy

class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('imagen',)

class FilesForm2(forms.ModelForm):
    class Meta:
        model = Files2 
        fields = ('imagen2',)

class FilesForm3(forms.ModelForm):
    class Meta:
        model = Files3 
        fields = ('imagen3',)


class FilesOutputForm(forms.ModelForm):
    class Meta:
        model = FilesOutput
        fields = ('imagenOutput',)


class FilesOutputForm2(forms.ModelForm):
    class Meta:
        model = FilesOutput2
        fields = ('imagenOutput2',)


class FilesOutputForm3(forms.ModelForm):
    class Meta:
        model = FilesOutput3
        # fields = ('imagenOutput3','in_file_1','in_file_2',)
        fields = ('imagenOutput3',)

