
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name="inicio"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('cursos/', cursos, name="cursos"),
    
    path('cursoform/', cursoForm, name="curso_form"),
    path('cursoform2/', cursoForm2, name="curso_form2"),
    path('profesorform/', profesorForm, name="profesor_form"),
    path('estudianteform/', estudianteForm, name="estudiante_form"),
    path('entregableform/', entregableForm, name="entregable_form"),
    
    path('buscar_comision/', buscarComision, name="buscar_comision"),
    path('buscar2/', buscar2, name="buscar2"),
]