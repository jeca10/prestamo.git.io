"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='C'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.desconectar, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('cumpu/',views.cumpu,name='cumpu'),
    path('create_compus/', views.createcompus, name='create_compus'),
    path('compus_detail/<int:compu_id>', views.compus_detail, name='compus_detail'),
    path('delete_Compu/<int:compu_id>', views.delete_Compu, name='delete_Compu'),
    path('aprendiz/',views.aprendiz,name='aprendiz'),
    path('create_aprendiz/',views.create_aprendiz,name='create_aprendiz'),
    path('aprendiz_detail/<int:apren_id>/',views.aprendiz_detail,name='aprendiz_detail'),
    path('delete_apend/<int:apren_id>/', views.delete_apend, name='delete_apend'),
    path('buscar/',views.listar_obje,name='buscar'),
    path('buscar2/',views.listar_obje_aprend,name='buscar2'),
    path('prestamo/',views.prestamo,name='prestamo'),
     path('crear_prestamo/',views.crear_prestamo,name='crear_prestamo'),
     path('delete_pres/<int:pres_id>/', views.delete_pres, name='delete_pres'),
]
