from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserProfileForm, UserUpdateForm



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if u_form.is_valid() and p_form.is_valid() and password_form.is_valid():
            u_form.save()
            p_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Mantiene la sesión activa después de cambiar la contraseña
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('profile')  # Redirigir a la página de perfil después de guardar
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)
        password_form = PasswordChangeForm(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'password_form': password_form
    }

    return render(request, 'profiles/profiles.html', context)
