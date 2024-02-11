from django import forms
from .models import Task, Compus

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'important']
        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-Check-input m-auto'})
            
        }


class CumposForm(forms.ModelForm):
    class Meta:
        model=Compus
        fields = ['marca', 'serial', 'descricion', ]
        widgets = {
        'marca' : forms.TextInput,
        'serial' : forms.Textarea,
        'descricion' : forms.Textarea

    }

        