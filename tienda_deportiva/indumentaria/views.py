from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Camiseta, Short, Botin
from .forms import CamisetaForm, BotinForm, ShortsForm
from django.contrib.auth.decorators import login_required

# Vista para mostrar todas las indumentarias
def indumentaria_lista(request):
    lista_camisetas = Camiseta.objects.all()  
    lista_shorts = Short.objects.all()        
    lista_botines = Botin.objects.all()       
 
    todas_las_indumentarias = list(lista_camisetas) + list(lista_shorts) + list(lista_botines)
    
    return render(request, 'indumentarias/indumentaria_lista.html', {"posts": todas_las_indumentarias})

# Vista para agregar una camiseta
@login_required
def agregar_camiseta(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES)
        if form.is_valid():
            camiseta = form.save(commit=False)
            camiseta.usuario = request.user  # Asocia la camiseta con el usuario autenticado
            camiseta.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = CamisetaForm()
    return render(request, 'indumentarias/agregar_camiseta.html', {'form': form})

# Vista para agregar un botín
@login_required
def agregar_botin(request):
    if request.method == 'POST':
        form = BotinForm(request.POST, request.FILES)  
        if form.is_valid():
            botin = form.save(commit=False)
            botin.usuario = request.user  # Asocia el botín con el usuario autenticado
            botin.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = BotinForm()
    return render(request, 'indumentarias/agregar_botin.html', {'form': form})

# Vista para agregar un short
@login_required
def agregar_shorts(request):
    if request.method == 'POST':
        form = ShortsForm(request.POST, request.FILES)  
        if form.is_valid():
            short = form.save(commit=False)
            short.usuario = request.user  # Asocia el short con el usuario autenticado
            short.save()
            return redirect('indumentaria_lista')  # Redirige a la lista de indumentaria
    else:
        form = ShortsForm()
    return render(request, 'indumentarias/agregar_shorts.html', {'form': form})

# Vista para editar una camiseta
@login_required
def editar_camiseta(request, id):
    camiseta = get_object_or_404(Camiseta, id=id)

    # Si la camiseta no tiene usuario, solo un superusuario puede editarla
    if camiseta.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")

    # Si la camiseta tiene usuario, verificar permisos
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

# Vista para editar un botín
@login_required
def editar_botin(request, id):
    botin = get_object_or_404(Botin, id=id)

    # Si el botín no tiene usuario, solo un superusuario puede editarlo
    if botin.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")
    
    # Si el botín tiene usuario, verificar permisos
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

# Vista para editar un short
@login_required
def editar_short(request, id):
    short = get_object_or_404(Short, id=id)

    # Si el short no tiene usuario, solo un superusuario puede editarlo
    if short.usuario is None:
        if not request.user.is_superuser:
            return HttpResponseForbidden("Solo un superusuario puede editar este artículo.")
    
    # Si el short tiene usuario, verificar permisos
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

# Vista para eliminar una camiseta
@login_required
def eliminar_camiseta(request, id):
    camiseta = get_object_or_404(Camiseta, id=id)

    # Permitir que los superusuarios siempre puedan eliminar
    if not request.user.is_superuser and request.user != camiseta.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        camiseta.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': camiseta})

# Vista para eliminar un botín
@login_required
def eliminar_botin(request, id):
    botin = get_object_or_404(Botin, id=id)

    # Permitir que los superusuarios siempre puedan eliminar
    if not request.user.is_superuser and request.user != botin.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        botin.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': botin})

# Vista para eliminar un short
@login_required
def eliminar_short(request, id):
    short = get_object_or_404(Short, id=id)

    # Permitir que los superusuarios siempre puedan eliminar
    if not request.user.is_superuser and request.user != short.usuario:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == 'POST':
        short.delete()
        return redirect('indumentaria_lista')
    
    return render(request, 'indumentarias/confirmar_eliminar.html', {'indumentaria': short})

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
