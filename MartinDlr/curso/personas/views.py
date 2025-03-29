from django.http import HttpResponse
from django.shortcuts import render
import datetime
from prueba.models import contactos

#def inicio(requerir):
#    #quiero retornar el contenido del archivo
#  return render(requerir, 'index.html')
"""
def inicio1(requerir):
  return HttpResponse('<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>pagina de prueba1</title></head><body></body>  <h1>plantilla html</h1>  <p>11contenido para mostrar: Lorem ipsum dolor sit amet consectetur, adipisicing elit. At minus nobis eum voluptas saepe ducimus, consequuntur consectetur placeat exercitationem veritatis hic modi blanditiis quia rerum iure impedit, ipsa illum non deserunt adipisci incidunt, quibusdam minima. Deleniti quam exercitationem quo? Veritatis ut corporis quisquam earum porro
  """

def obtener_fecha_actual(requiere_fecha):
  #obtener fecha de sistema
  ahora = datetime.datetime.now()
  #combinacion de texto y variables o renderizar.
  return render (requiere_fecha,'fecha_actual.html', {'fecha_actual_tmp': ahora})


def inicio(requerir):
  return HttpResponse('<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>pagina de prueba</title></head><body></body>  <h1>plantilla html</h1>  <p>contenido para mostrar: Lorem ipsum dolor sit amet consectetur, adipisicing elit. At minus nobis eum voluptas saepe ducimus, consequuntur consectetur placeat exercitationem veritatis hic modi blanditiis quia rerum iure impedit, ipsa illum non deserunt adipisci incidunt, quibusdam minima. Deleniti quam exercitationem quo? Veritatis ut corporis quisquam earum porro, dolorem reprehenderit laudantium consectetur mollitia!</p></html>')
def hola(request):
  return HttpResponse('<h1> hola estudiantes del curso python nivel4 </h1>')

def principal(requerido):
  return render(requerido, 'index.html')

def personas_ingresar(requerido):
  return render(requerido, 'ingresar.html')

def personas_ingresar01(requerido):
  mensajes = []
  if requerido.method == 'POST':
    tnombre = requerido.POST.get('nombre')
    tapellido = requerido.POST.get('apellido')
    tcorreo  = requerido.POST.get('correo')
    ttelefono = requerido.POST.get('telefono')
    nuevocontacto = contactos(nombre=tnombre,apellido=tapellido, correo=tcorreo, telefono=ttelefono)
    nuevocontacto.save()
    mensajes.append('Contacto agregado OK')
    return render(requerido, 'ingresar.html', {'mensajes': mensajes})
