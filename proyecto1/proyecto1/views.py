from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render



class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #Primera vista

    p1 = Persona("Sergio Andrés", "Soto Cano")

    #doc_externo=open("F:/proyectos/training_Django_PI/proyecto1/proyecto1/templates/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template('miplantilla.html')
    #contexto=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido})
    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido})
    
    return render(request,"miplantilla.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido})

def fecha_hoy(request):
    
    fecha=datetime.datetime.now()

    muestra_fecha="<html><body><h2>Fecha y hora actual: %s </h2></body></html>" %fecha

    return HttpResponse(muestra_fecha)

def calculaEdad(request, edad, year):
    
    #edadActual=25
    periodo=year-2019
    edadFutura=edad+periodo
    muestraEdad="<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(year, edadFutura)

    return HttpResponse(muestraEdad)

def cursoC(request):
    fecha=datetime.datetime.now()
    
    return render(request, "cursoC.html", {"fecha_hoy":fecha})
