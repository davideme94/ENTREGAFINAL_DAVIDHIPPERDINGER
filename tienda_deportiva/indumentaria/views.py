from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Camiseta, Short, Botin
from .forms import CamisetaForm, BotinForm, ShortsForm

# Vista para mostrar todas las indumentarias
def indumentaria_lista(request):
    lista_camisetas = Camiseta.objects.all()  
    lista_shorts = Short.objects.all()        
    lista_botines = Botin.objects.all()       
 
    todas_las_indumentarias = list(lista_camisetas) + list(lista_shorts) + list(lista_botines)
    
    return render(request, 'indumentarias/indumentaria_lista.html', {"posts": todas_las_indumentarias})

# Vista para agregar una camiseta
def agregar_camiseta(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = CamisetaForm()
    return render(request, 'indumentarias/agregar_camiseta.html', {'form': form})

# Vista para agregar un botín
def agregar_botin(request):
    if request.method == 'POST':
        form = BotinForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = BotinForm()
    return render(request, 'indumentarias/agregar_botin.html', {'form': form})

# Vista para agregar un short
def agregar_shorts(request):
    if request.method == 'POST':
        form = ShortsForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = ShortsForm()
    return render(request, 'indumentarias/agregar_shorts.html', {'form': form})

# Vista para mostrar la búsqueda por tipo
def busquedatipo(request):
    return render(request, "indumentarias/busquedatipo.html")

# Vista para realizar la búsqueda de indumentaria por tipo
def buscar(request):
    if request.GET.get("tipo"):
        tipo = request.GET["tipo"]

        camisetas = Camiseta.objects.filter(tipo__icontains=tipo)
        shorts = Short.objects.filter(tipo__icontains=tipo)
        botines = Botin.objects.filter(tipo__icontains=tipo)

        resultados = list(camisetas) + list(shorts) + list(botines)

        return render(request, "indumentarias/resultadobusqueda.html", {"resultados": resultados, "tipo": tipo})
    else:
        return HttpResponse("No enviaste datos")
