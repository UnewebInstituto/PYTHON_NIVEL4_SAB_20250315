from django.http import HttpResponse

def hola(request):
  return HttpResponse('<h1>Hola Estudiantes del curso de Python Nivel 4<h1>')