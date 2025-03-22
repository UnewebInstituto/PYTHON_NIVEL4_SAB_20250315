from django.http import  HttpResponse
from django.shortcuts import render
import datetime


def inicio(request):
    return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body>  <h1>Plantilla HTML</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet suscipit odit quasi veniam? Natus libero iste ab ratione, delectus dolore commodi perferendis voluptas atque voluptatem vitae quisquam consectetur voluptatibus rem suscipit consequuntur doloribus voluptate quidem, laborum impedit blanditiis, nesciunt assumenda aliquid. Similique at quidem earum cupiditate asperiores cumque quisquam facere!</p></body></html>')


def hola(request):
    return HttpResponse('<h1>Hola estudiantes del curso de Python nivel 4</h1>')

"""
def inicio1(request):
    return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body>  <h1>Plantilla HTML inicio 1</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet suscipit odit quasi veniam? Natus libero iste ab ratione, delectus dolore commodi perferendis voluptas atque voluptatem vitae quisquam consectetur voluptatibus rem suscipit consequuntur doloribus voluptate quidem, laborum impedit blanditiis, nesciunt assumenda aliquid. Similique at quidem earum cupiditate asperiores cumque quisquam facere!</p></body></html>')'''
"""

def fecha_actual_nueva(request):
    ahora=datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual_tmp':ahora})

def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
    return render (request, 'ingresar.html')