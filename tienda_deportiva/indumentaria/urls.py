# indumentaria/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.indumentaria_lista, name='indumentaria_lista'),
    path('agregar-camiseta/', views.agregar_camiseta, name='agregar_camiseta'),
    path('agregar-botin/', views.agregar_botin, name='agregar_botin'),
    path('agregar-shorts/', views.agregar_shorts, name='agregar_shorts'),
    path('busquedatipo/', views.busquedatipo, name='busquedatipo'),
    path('resultadobusqueda/', views.buscar, name='resultadobusqueda'),
]
