from django import forms
from .models import Task, Compus, Aprendiz, Prestamo

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


class AprendizForm(forms.ModelForm):
    class Meta:
        model=Aprendiz
        fields = ['Nombre', 'Documento', 'Formacion', 'Ficha', ]
        widgets = {
        'Nombre' : forms.TextInput,
        'Documento' : forms.Textarea,
        'Formacion' : forms.Textarea,
        'Ficha' : forms.Textarea

    }
    

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['Documento', 'Serial', 'Descripcion' , 'hora_inicio',]
        widgets = {
            'documento' : forms.TextInput,
            'serial' : forms.TextInput,
            'Descripcion' : forms.Textarea,
            'hora_inicio' : forms.DateTimeInput,
            
        }
    