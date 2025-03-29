from django.http import HttpResponse
import datetime
from django.shortcuts import render

from prueba.models import Contactos

def inicio(request):
  return HttpResponse('<!DOCTYPE html><html lang=en><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Plantilla HTML</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta tempore sed consequuntur perferendis debitis ratione, quisquam labore iusto aliquid esse adipisci vero provident assumenda odit. Enim quam quod minus! Facilis sequi consectetur consequuntur magnam fugiat! Tempore perferendis fuga hic sed labore, deserunt, dolorem sit inventore similique explicabo quam incidunt facere.</p></body></html>')

"""def inicio1(request):
  return HttpResponse('<!DOCTYPE html><html lang=en><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Plantilla HTML 1</h1><p>Contenido a mostrar: Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta tempore sed consequuntur perferendis debitis ratione, quisquam labore iusto aliquid esse adipisci vero provident assumenda odit. Enim quam quod minus! Facilis sequi consectetur consequuntur magnam fugiat! Tempore perferendis fuga hic sed labore, deserunt, dolorem sit inventore similique explicabo quam incidunt facere 1.</p></body></html>')"""
  
def obtener_fecha_actual(request):
    # Obtener fecha del sistema
    ahora = datetime.datetime.now()
    # combinación de plantilla y contexto
    return render(request,'fecha_actual.html', {'fecha_actual_tmp':ahora})

def hola(request):
    return HttpResponse('<h1>Hola estudiantes del curso de Python nivel 4</h1>')
  
def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
  return render(request, 'ingresar.html')

def personas_ingresar01(request):
  mensajes = []
  if request.method == 'POST':
    nom = request.POST.get('nombre')
    ape = request.POST.get('apellido')
    cor = request.POST.get('correo')
    tel = request.POST.get('telefono')
    nvo_contacto = Contactos(nombre=nom, apellido=ape, correo=cor, telefono=tel)
    
  nvo_contacto.save()
  
  mensajes.append('Contacto ingresado con exito')
  return render(request, 'Ingresar.html', {'mensaje':mensajes})
