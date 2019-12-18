from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
    
    return HttpResponse("Hola Mundo, esta es nuestra primera página con Django.")

def fecha_hoy(request):
    
    fecha=datetime.datetime.now()

    muestra_fecha="<html><body><h2>Fecha y hora actual: %s </h2></body></html>" %fecha

    return HttpResponse(muestra_fecha)