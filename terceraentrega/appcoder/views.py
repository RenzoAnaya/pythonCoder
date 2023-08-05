from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,"appcoder/base.html")

def profesores(request):
    ctx={"profesores": Profesor.objects.all()}
    return render(request,"appcoder/profesores.html", ctx)

def estudiantes(request):
    ctx={"estudiantes": Estudiante.objects.all()}
    return render(request,"appcoder/estudiantes.html", ctx)

def entregables(request):
    ctx={"entregables": Entregable.objects.all()}
    return render(request,"appcoder/entregables.html", ctx)

def cursos(request):
    ctx={"cursos": Curso.objects.all()}
    return render(request,"appcoder/cursos.html", ctx)

def cursoForm(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST['nombre'], comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Se grabo el curso")
    return render(request, "appcoder/cursoForm.html")

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


def profesorForm(request):
    if request.method == "POST":
        profesorForm = ProfesorForm(request.POST)
        if profesorForm.is_valid():
            informacion = profesorForm.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            profesor.save()
            return render(request, 'appcoder/base.html')
    else:
        profesorForm = ProfesorForm()
    return render(request,"appcoder/profesorForm.html",{'form':profesorForm})


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

def buscarComision(request):
    return render(request, "appcoder/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        if not cursos:
            return HttpResponse("No se encontraron cursos")
        return render(request, "appcoder/resultadosComision.html", 
                      {"comision": comision, "cursos": cursos})
    return HttpResponse("No se ingresaron datos")
    