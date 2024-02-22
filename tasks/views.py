from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q
from .forms import TaskForm, CumposForm, AprendizForm
from .models import Task,Compus, Aprendiz
from django.utils import timezone
import re

# Create your views here.
def home(request):
    return render(request, 'home.html',)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Validar contraseña con expresión regular
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$', password):
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especial.'
                })

            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': form,
                'error': 'La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especial.'
            })
    else:
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
       

def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tareas/tasks.html', {"tasks": tasks})

def create_task(request):
    if request.method == "GET":
        return render(request, 'tareas/create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form=TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tareas/create_task.html', {
                'form': TaskForm,
                "error": 'Error al crear la tarea'
            })

def desconectar(request):
    logout(request)
    return redirect('home')

def task_detail(request, task_id):
   if request.method == "GET":
        task =get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'tareas/task_detail.html', {'task': task, 'form': form})
   else:
      try:
            task =get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
      except ValueError:
            return render(request, 'tareas/task_detail.html', {'task': task, 'form': form,
            'error': "error al actualizar"    
            })


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('/')
 

def cumpu(request):
    compus=Compus.objects.all()
    return render(request,'Computador/compus.html',{'compus':compus})


def createcompus(request):
    if request.method == 'GET':
        return render(request, 'Computador/create_compus.html', {
            'form': CumposForm
        })
    else:
        try:
            form=CumposForm(request.POST)
            form.save()
            return redirect('cumpu')
        except ValueError:
            return render(request, 'Computador/create_compus.html', {
                'form': CumposForm,
                "error": 'Error al crear el compu'
            })


def compus_detail(request, compu_id):
   if request.method == "GET":
        compu =get_object_or_404(Compus, pk=compu_id)
        form = CumposForm(instance=compu)
        return render(request, 'Computador/compu_detail.html', {'compus': compu, 'form': form})
   else:
      try:
            compu =get_object_or_404(Compus, pk=compu_id)
            form = CumposForm(request.POST, instance=compu)
            form.save()
            return redirect('cumpu')
      except ValueError:
            return render(request, 'Computador/compu_detail.html', {'compus': compu, 'form': form,
            'error': "error al actualizar"    
            })


def delete_Compu(request, compu_id):
    compus = get_object_or_404(Compus, pk=compu_id)
    if request.method == 'GET':
        compus.delete()
        return redirect('cumpu')

def aprendiz(request):
    aprendiz=Aprendiz.objects.all()
    return render(request, 'Aprendiz/aprendiz.html',{'aprendiz':aprendiz})

def create_aprendiz(request):
    if request.method == 'GET':
        return render(request, 'Aprendiz/create_apre.html', {
            'form': AprendizForm
        })
    else:
        try:
            form=AprendizForm(request.POST)
            form.save()
            return redirect('aprendiz')
        except ValueError:
            return render(request, 'Aprendiz/create_apre.html', {
                'form': AprendizForm,
                "error": 'Error al crear el Aprendiz'
            })

def aprendiz_detail(request, apren_id):
    if request.method == "GET":
        apren = get_object_or_404(Aprendiz, pk=apren_id)
        form = AprendizForm(instance=apren)
        return render(request, 'Aprendiz/apren_detail.html',
                      {'aprendiz':apren, 'form':form,
                       'error':"error al actualizar"
                       })
    else: 
        try:
            apren = get_object_or_404(Aprendiz, pk=apren_id)
            form = AprendizForm(request.POST, instance=apren)
            form.save()
            return redirect('aprendiz')
        except ValueError:
            return render(request, 'Aprendiz/apren_detail.html', {'aprendiz':apren, 'form':form,
                       'error':"error al actualizar"
                       })

def delete_apend(request, apren_id):
    apren = get_object_or_404(Aprendiz, pk=apren_id)
    if request.method == 'GET':
        apren.delete()
        return redirect('aprendiz')




def listar_obje(request):
    busqueda = request.POST.get('busqueda')
    buscar =  Compus.objects.all()

    if busqueda:
        compu = compu.filter(
            Q(serial__icontains=busqueda )|
            Q(marca__icontains=busqueda) 
        ).distinct()

    return render(request, 'Computador/compus.html', {'compu': buscar})