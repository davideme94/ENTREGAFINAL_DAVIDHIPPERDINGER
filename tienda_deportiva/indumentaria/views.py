from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Camiseta, Short, Botin
from .forms import CamisetaForm, BotinForm, ShortsForm
from django.contrib.auth.decorators import login_required


def indumentaria_lista(request):
    lista_camisetas = Camiseta.objects.all()  
    lista_shorts = Short.objects.all()        
    lista_botines = Botin.objects.all()       
 
    todas_las_indumentarias = list(lista_camisetas) + list(lista_shorts) + list(lista_botines)
    
    return render(request, 'indumentarias/indumentaria_lista.html', {"posts": todas_las_indumentarias})


@login_required
def agregar_camiseta(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES)
        if form.is_valid():
            camiseta = form.save(commit=False)
            camiseta.usuario = request.user  
            camiseta.save()
            return redirect('indumentaria_lista')  
    else:
        form = CamisetaForm()
    return render(request, 'indumentarias/agregar_camiseta.html', {'form': form})


@login_required
def agregar_botin(request):
    if request.method == 'POST':
        form = BotinForm(request.POST, request.FILES)  
        if form.is_valid():
            botin = form.save(commit=False)
            botin.usuario = request.user  
            botin.save()
            return redirect('indumentaria_lista')  
    else:
        form = BotinForm()
    return render(request, 'indumentarias/agregar_botin.html', {'form': form})


@login_required
def agregar_shorts(request):
    if request.method == 'POST':
        form = ShortsForm(request.POST, request.FILES)  
        if form.is_valid():
            short = form.save(commit=False)
            short.usuario = request.user  
            short.save()
            return redirect('indumentaria_lista')  
    else:
        form = ShortsForm()
    return render(request, 'indumentarias/agregar_shorts.html', {'form': form})


@login_required
def editar_camiseta(request, id):
    camiseta = get_object_or_404(Camiseta, id=id)

    
    if camiseta.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")

    
    elif not request.user.is_superuser and request.user != camiseta.usuario:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES, instance=camiseta)
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')
    else:
        form = CamisetaForm(instance=camiseta)
    
    return render(request, 'indumentarias/editar_camiseta.html', {'form': form})


@login_required
def editar_botin(request, id):
    botin = get_object_or_404(Botin, id=id)

    
    if botin.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")
    
    
    elif not request.user.is_superuser and request.user != botin.usuario:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == 'POST':
        form = BotinForm(request.POST, request.FILES, instance=botin)
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')
    else:
        form = BotinForm(instance=botin)

    return render(request, 'indumentarias/editar_botin.html', {'form': form})


@login_required
def editar_short(request, id):
    short = get_object_or_404(Short, id=id)

    
    if short.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")
    
    
    elif not request.user.is_superuser and request.user != short.usuario:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == 'POST':
        form = ShortsForm(request.POST, request.FILES, instance=short)
        if form.is_valid():
            form.save()
            return redirect('indumentaria_lista')
    else:
        form = ShortsForm(instance=short)

    return render(request, 'indumentarias/editar_short.html', {'form': form})


@login_required
def eliminar_camiseta(request, id):
    camiseta = get_object_or_404(Camiseta, id=id)

    
    if not request.user.is_superuser and request.user != camiseta.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        camiseta.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': camiseta})


@login_required
def eliminar_botin(request, id):
    botin = get_object_or_404(Botin, id=id)

    
    if not request.user.is_superuser and request.user != botin.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        botin.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': botin})


@login_required
def eliminar_short(request, id):
    short = get_object_or_404(Short, id=id)

    
    if not request.user.is_superuser and request.user != short.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        short.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': short})


def busquedatipo(request):
    return render(request, "indumentarias/busquedatipo.html")


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
