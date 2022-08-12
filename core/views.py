from django.shortcuts import render

def holamundoCore(request):
    return render(request, 'core.html')

def noticias(request):
    return render(request, 'noticias.html')

def deportes(request):
    return render(request, 'deportes.html')


################# HERENCIAAA###################
def inicio(request):
    return render(request, 'herencias/inicio.html')

def quienes_somos(request):
    return render(request, 'herencias/quienes_somos.html')

def nuestro_producto(request):
    return render(request, 'herencias/nuestro_producto.html')

def contacto(request):
    return render(request, 'herencias/contacto.html')

def quienes_somos1(request):
    return render(request, 'herencias/quienes_somos1.html')