from django.forms import *
from .models import Task, Compus, Aprendiz, Prestamo

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'important']
        widgets= {
            'title' : TextInput(attrs={'class' : 'form-control'}),
            'description' : Textarea(attrs={'class' : 'form-control'}),
            'important' : CheckboxInput(attrs={'class' : 'form-Check-input m-auto'})
            
        }


class CumposForm(ModelForm):
    class Meta:
        model=Compus
        fields = ['marca', 'serial', 'descricion', ]
        widgets = {
        'marca' : TextInput,
        'serial' : Textarea,
        'descricion' : Textarea

    }


class AprendizForm(ModelForm):
    class Meta:
        model=Aprendiz
        fields = ['Nombre', 'Documento', 'Formacion', 'Ficha', ]
        widgets = {
        'Nombre' : TextInput,
        'Documento' : Textarea,
        'Formacion' : Textarea,
        'Ficha' : Textarea
    }
        

class PrestamoForm(forms.Form):
    Documento = ModelChoiceField(queryset=Aprendiz.objects.order_by("Documento").all(), label="Documento")
    Serial = IntegerField(label="Serial")
    Descripcion = CharField(label="Descripcion")
    
    