from django.http import HttpResponse

def saludo(request): #Primera vista
    
    return HttpResponse("Hola Mundo, esta es nuestra primera página con Django.")