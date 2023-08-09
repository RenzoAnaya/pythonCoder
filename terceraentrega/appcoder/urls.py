
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name="inicio"),
    
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('cursos/', cursos, name="cursos"),
    
    path('cursoform/', cursoForm, name="curso_form"),
    path('cursoform2/', cursoForm2, name="curso_form2"),
   
    path('estudianteform/', estudianteForm, name="estudiante_form"),
    path('entregableform/', entregableForm, name="entregable_form"),
    
    path('buscar_comision/', buscarComision, name="buscar_comision"),
    path('buscar2/', buscar2, name="buscar2"),
    
    path('profesores/', profesores, name="profesores"),
    path('profesorform/', profesorForm, name="profesor_form"),
    path('update_profesor/<id_profesor>/', updateProfesor, name="update_profesor"),
    path('delete_profesor/<id_profesor>/', deleteProfesor, name="delete_profesor"),
    
#.. Class Based
    path('estudiantes2/', EstudianteList.as_view(), name="estudiantes2"),
    path('create_estudiante/', EstudianteCreate.as_view(), name="create_estudiante"),    
    path('detail_estudiante/<int:pk>/', EstudianteDetail.as_view(), name="detail_estudiante"),   
    path('update_estudiante/<int:pk>/', EstudianteUpdate.as_view(), name="update_estudiante"), 
    path('delete_estudiante/<int:pk>/', EstudianteDelete.as_view(), name="delete_estudiante"),  
    
#'''' login
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="appcoder/logout.html"), name="logout"),
    path('register/', register, name="register"),
    
    
#..... editar
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    
#..... avatar
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]