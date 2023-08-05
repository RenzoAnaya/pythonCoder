from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from appcoder.models import Curso, Familiar
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola Mundo!')

def bienvenida(request):
    return HttpResponse("<html><h1>Bienvenidos a Django con Python!</h1></html>")

def diaDeHoy(request):
    hoy = datetime.date.today() # Obtenemos la fecha actual del sistema oper
    respuestaDia = f"Hoy es : <br> {hoy}"
    return HttpResponse(respuestaDia)

def saludoPersonal(request, nombre):
    saludo = f"Bienvenido {nombre}"
    return HttpResponse(saludo)

def home(request):
    plantilla = loader.get_template("index.html")
        
    datos = {
        'nombre':'Juan',
        'apellido': 'Rodriguez',
        'dni':74566621,
        'fecha_hoy': datetime.datetime.now(),
        'notas' : [9,9,8,7,6]
    }
    
    documento = plantilla.render(datos)
    return HttpResponse(documento)
    
    
def crear_curso(request, pnombre, pcomision):
    curso = Curso(nombre=pnombre, comision=pcomision)
    curso.save()
    
    respuesta = f"El curso creado fue {curso.nombre} de la comisión {curso.comision}"
    return HttpResponse(respuesta)


    
def ver_familiares(request):
    plantilla = loader.get_template("familiares.html")
    
    
    yo = Familiar.objects.create(
        nombre='Juan', 
        apellido_paterno='Rodriguez',
        apellido_materno='Lopez', 
        fecha_de_nacimiento=datetime.date(1990, 1, 1), 
        edad_de_matrimonio=25, 
        rol='yo'
    )
    hijo = Familiar.objects.create(
        nombre='Pablo', 
        apellido_paterno='Rodriguez',
        apellido_materno='Lopez', 
        fecha_de_nacimiento=datetime.date(2015, 1, 1), 
        rol='hijo'
    )
    padre = Familiar.objects.create(
        nombre='Carlos', 
        apellido_paterno='Rodriguez',
        apellido_materno='Perez', 
        fecha_de_nacimiento=datetime.date(1965, 1, 1), 
        edad_de_matrimonio=24,
        rol='padre'
    )
    madre = Familiar.objects.create(
        nombre='Maria', 
        apellido_paterno='Gomez',
        apellido_materno='Sanchez', 
        fecha_de_nacimiento=datetime.date(1967, 1, 1), 
        edad_de_matrimonio=23, 
        rol='madre'
    )
    abuelo_paterno = Familiar.objects.create(
        nombre='Roberto', 
        apellido_paterno='Rodriguez',
        apellido_materno='Mendoza', 
        fecha_de_nacimiento=datetime.date(1940, 1, 1), 
        edad_de_matrimonio=22,
        rol='abuelo_paterno'
    )
    abuela_paterna = Familiar.objects.create(
        nombre='Rosa', 
        apellido_paterno='Gomez',
        apellido_materno='Vargas', 
        fecha_de_nacimiento=datetime.date(1942, 1, 1), 
        edad_de_matrimonio=21, 
        rol='abuela_paterna'
    )

    yo.padres.add(padre, madre)
    hijo.padres.add(yo)
    padre.padres.add(abuelo_paterno, abuela_paterna)
    
    datos = {'familiar': yo}
    
    documento = plantilla.render(datos)
    return HttpResponse(documento)
