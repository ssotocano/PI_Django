from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
    
    return HttpResponse("Hola Mundo, esta es nuestra primera página con Django.")

def fecha_hoy(request):
    
    fecha=datetime.datetime.now()

    muestra_fecha="<html><body><h2>Fecha y hora actual: %s </h2></body></html>" %fecha

    return HttpResponse(muestra_fecha)

def calculaEdad(request, year):
    
    edadActual=25
    periodo=year-2019
    edadFutura=edadActual+periodo
    muestraEdad="<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(year, edadFutura)

    return HttpResponse(muestraEdad)

