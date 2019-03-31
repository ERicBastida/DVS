from django import forms

from .models import Files, Files2, Files3
#from django.forms import modelformset_factory, formset_factory
#import extra_views
class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('imagen',)
    

#FilesFormSet = modelformset_factory(Files,form=FilesForm)

class FilesForm2(forms.ModelForm):
    class Meta:
        model = Files2 
        fields = ('imagen2',)

class FilesForm3(forms.ModelForm):
    class Meta:
        model = Files3 
        fields = ('imagen3',)

