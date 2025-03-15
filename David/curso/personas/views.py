from django.http import HttpResponse
def hola(request):
  return HttpResponse('<h1>Hola estudiantes del curso Python nivel 4')