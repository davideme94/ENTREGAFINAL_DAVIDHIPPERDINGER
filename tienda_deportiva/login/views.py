from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login/login.html'  # Usa una plantilla personalizada para el login

