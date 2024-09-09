from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('indumentaria/', include('indumentaria.urls')),
    path('signup/', include('registration.urls')),
    path('login/', include('login.urls')),
    path('profile/', include('profiles.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)