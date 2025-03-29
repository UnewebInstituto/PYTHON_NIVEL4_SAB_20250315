from django.http import HttpResponse
from django.shortcuts import render
from prueba.models import contactos
import datetime

def inicio(request):
  return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Plantilla</h1><p>NO HIZO NADA Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam deserunt molestiae, itaque laboriosam vel aperiam cum esse pariatur, rem dolore obcaecati, dignissimos id veniam numquam. Assumenda tempora accusamus dolorem deserunt alias asperiores, vitae expedita consectetur deleniti blanditiis. Aspernatur reiciendis reprehenderit doloremque nemo amet est corrupti numquam illo delectus, sunt praesentium.</p></body></html>')

  """
  
def inicio1(request):
  return HttpResponse('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Plantilla INICIO 1</h1><p>NO HIZO NADA Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam deserunt molestiae, itaque laboriosam vel aperiam cum esse pariatur, rem dolore obcaecati, dignissimos id veniam numquam. Assumenda tempora accusamus dolorem deserunt alias asperiores, vitae expedita consectetur deleniti blanditiis. Aspernatur reiciendis reprehenderit doloremque nemo amet est corrupti numquam illo delectus, sunt praesentium.</p></body></html>')
"""
def hola(request):
  return HttpResponse('<h1>Hola Estudiantes del curso de Python Nivel 4<h1>')
  
  
def obtener_fecha_actual(request):
  ahora = datetime.datetime.now()
  return render(request,'fecha_actual.html',{'fecha_actual_tmp':ahora}) 
  
  
def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
  return render(request,'ingresar.html')
def personas_ingresar01(request):
  mensajes = []
  if request.method == 'POST':
    nom = request.POST.get('nombre')
    ape = request.POST.get('apellido')
    cor = request.POST.get('correo')
    tel = request.POST.get('telefono')
    nvo_contacto = contactos(nombre=nom,apellido=ape,correo=cor,telefono=tel)
    nvo_contacto.save()
    mensajes.append('Contacto ha ingresado con Exito')
    return render(request, 'ingresar.html',{'mensajes':mensajes})
    