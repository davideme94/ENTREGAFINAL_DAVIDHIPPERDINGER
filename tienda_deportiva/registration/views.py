from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SimpleUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada exitosamente!")
            return redirect('homepage') 
        else:
            messages.error(request, "Error al crear la cuenta. Asegúrate de que todos los campos sean correctos.")
    else:
        form = SimpleUserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})
