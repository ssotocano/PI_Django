from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): #Primera vista

    doc_externo=open("D:/django_projects/PI_Django/proyecto1/proyecto1/templates/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    contexto=Context()
    documento=plt.render(contexto)
    
    return HttpResponse(documento)

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

