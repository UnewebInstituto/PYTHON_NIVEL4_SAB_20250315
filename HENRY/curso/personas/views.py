from django.http import HttpResponse
import datetime
from django.shortcuts import render

def inicio(request):
    return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body>  <h1>Plantilla HTML</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet suscipit odit quasi veniam? Natus libero iste ab ratione, delectus dolore commodi perferendis voluptas atque voluptatem vitae quisquam consectetur voluptatibus rem suscipit consequuntur doloribus voluptate quidem, laborum impedit blanditiis, nesciunt assumenda aliquid. Similique at quidem earum cupiditate asperiores cumque quisquam facere!</p></body></html>')

"""
def inicio1(request):
    return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body>  <h1>Plantilla HTML INICIO 1</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet suscipit odit quasi veniam? Natus libero iste ab ratione, delectus dolore commodi perferendis voluptas atque voluptatem vitae quisquam consectetur voluptatibus rem suscipit consequuntur doloribus voluptate quidem, laborum impedit blanditiis, nesciunt assumenda aliquid. Similique at quidem earum cupiditate asperiores cumque quisquam facere!</p></body></html>')
"""

def obtener_fecha_actual(request):
    # Obtener fecha del sistema
    ahora = datetime.datetime.now()
    # combinación de plantilla y contexto
    return render(request,'fecha_actual.html',{'fecha_actual_tmp':ahora})

def hola(request):
    return HttpResponse('<h1>Hola estudiantes del curso de Python nivel 4</h1>')

def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
  return render(request,'ingresar.html')