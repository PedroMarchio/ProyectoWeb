from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    miHTML = open('C:/Users/Raimundo/Escritorio/EntregaFinal/projectEF/projectEF/plantillas/template.html')
    plantilla = Template(miHTML.read())
    miHTML.close()

    miContexto = Context()
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)