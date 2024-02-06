from django.contrib import admin
from .models import Task, Compus, Aprendiz

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(Aprendiz)
admin.site.register(Compus)