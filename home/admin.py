from django.contrib import admin
from .models import Profesores, Alumnos, Aulas, Carreras, Materias

# Register your models here.
admin.site.register(Profesores)
admin.site.register(Alumnos)
admin.site.register(Aulas)
admin.site.register(Carreras)
admin.site.register(Materias)