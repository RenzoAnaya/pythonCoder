from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"appcoder/base.html")


@login_required
def estudiantes(request):
    ctx={"estudiantes": Estudiante.objects.all()}
    return render(request,"appcoder/estudiantes.html", ctx)

@login_required
def entregables(request):
    ctx={"entregables": Entregable.objects.all()}
    return render(request,"appcoder/entregables.html", ctx)

@login_required
def cursos(request):
    ctx={"cursos": Curso.objects.all()}
    return render(request,"appcoder/cursos.html", ctx)

@login_required
def cursoForm(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST['nombre'], comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Se grabo el curso")
    return render(request, "appcoder/cursoForm.html")

@login_required
def cursoForm2(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'appcoder/base.html') 
    else:
        miForm = CursoForm()
    
    return render(request, "appcoder/cursoForm2.html",{"form":miForm})

@login_required
def profesorForm(request):
    if request.method == "POST":
        profesorForm = ProfesorForm(request.POST)
        if profesorForm.is_valid():
            informacion = profesorForm.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                apellido = informacion['apellido'], 
                                email = informacion['email'],
                                profesion = informacion['profesion'])
            profesor.save()
            return redirect(reverse_lazy('profesores'))
    else:
        profesorForm = ProfesorForm()
    return render(request,"appcoder/profesorForm.html",{'form':profesorForm})

@login_required
def estudianteForm(request):
    if request.method == "POST":
        estudianteForm = EstudianteForm(request.POST)
        if estudianteForm.is_valid():
            informacion = estudianteForm.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            estudiante.save()
            return render(request, 'appcoder/base.html')
    else:
        estudianteForm = EstudianteForm()
    return render(request,"appcoder/estudianteForm.html",{'form':estudianteForm})
    
@login_required
def entregableForm(request):
    if request.method == "POST":
        entregableForm = EntregableForm(request.POST)
        if entregableForm.is_valid():
            informacion = entregableForm.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], fechaEntrega = informacion['fechaEntrega'], entregado = informacion['entregado'])
            entregable.save()
            return render(request, 'appcoder/base.html')
    else:
        entregableForm = EntregableForm()
    return render(request,"appcoder/entregableForm.html",{'form':entregableForm})

@login_required
def buscarComision(request):
    return render(request, "appcoder/buscarComision.html")

@login_required
def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        if not cursos:
            return HttpResponse("No se encontraron cursos")
        return render(request, "appcoder/resultadosComision.html", 
                      {"comision": comision, "cursos": cursos})
    return HttpResponse("No se ingresaron datos")
    
@login_required   
def profesores(request):
    ctx={"profesores": Profesor.objects.all()}
    return render(request,"appcoder/profesores.html", ctx)

@login_required
def updateProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        profesorForm = ProfesorForm(request.POST)
        if profesorForm.is_valid():
            profesor.nombre =  profesorForm.cleaned_data.get('nombre')
            profesor.apellido =  profesorForm.cleaned_data.get('apellido')
            profesor.email =  profesorForm.cleaned_data.get('email')
            profesor.profesion =  profesorForm.cleaned_data.get('profesion')
            profesor.save()
            return redirect(reverse_lazy('profesores'))
    else:
        profesorForm = ProfesorForm(initial={'nombre':profesor.nombre,
                                             'apellido':profesor.apellido,
                                             'email':profesor.email,
                                             'profesion':profesor.profesion})
    return render(request, "appcoder/profesorForm.html",{'form':profesorForm})

@login_required
def deleteProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    return redirect(reverse_lazy('profesores'))
            
            
#---- Class based

class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante
    
class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes2')
    
class EstudianteDetail(LoginRequiredMixin, DetailView):
    model = Estudiante
    
class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes2')
    
class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes2')
    
    
#---- Login, Logout, Registracion

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                
                #ACA INTENTAMOS LEER EL AVATAR
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                
                return render(request, "appcoder/base.html", {"form":form, "mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "appcoder/login.html", {"form":form, "mensaje":"Usuario o clave incorrectos"})
        else:
            return render(request, 'appcoder/login.html', {"form":form, "mensaje":"Datos Inválidos"})
    else:
        form = AuthenticationForm
        return render(request, "appcoder/login.html",{"form":form})


def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "appcoder/base.html", {"mensaje":"Usuario creado"})
    else:
        form = RegistroUsuariosForm()
    return render(request, "appcoder/registro.html", {"form":form})
            
            


#---- registracion de usuarios
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "appcoder/base.html", {"mensaje":"Usuario actualizado"})
        else:
            return render(request, "appcoder/editarPerfil.html", {'form':form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "appcoder/editarPerfil.html", {'form':form, 'usuario':usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            # BORRO AVATAR ANTERIOR
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                if avatarViejo[0].imagen.url != "ruta/de/la/imagen/default.jpg":  # Cambia esta ruta por la ruta de tu imagen por defecto
                    avatarViejo[0].imagen.delete(save=False)  # Elimina solo la imagen
                    avatarViejo[0].delete()  # Elimina el objeto avatar
                
            # GRABO NUEVO AVATAR
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()  
            
            # ALMACENAR EN SESSION LA URL PARA MOSTRARLA
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
                
            return render(request, "appcoder/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "appcoder/agregarAvatar.html", {'form':form})
            