from django.urls import path
from . import views

urlpatterns = [
    path('', views.indumentaria_lista, name='indumentaria_lista'),
    
    
    path('agregar-camiseta/', views.agregar_camiseta, name='agregar_camiseta'),
    path('agregar-botin/', views.agregar_botin, name='agregar_botin'),
    path('agregar-shorts/', views.agregar_shorts, name='agregar_shorts'),
    
    
    path('camiseta/editar/<int:id>/', views.editar_camiseta, name='editar_camiseta'),
    path('botin/editar/<int:id>/', views.editar_botin, name='editar_botin'),
    path('short/editar/<int:id>/', views.editar_short, name='editar_short'),
    
    
    path('camiseta/eliminar/<int:id>/', views.eliminar_camiseta, name='eliminar_camiseta'),
    path('botin/eliminar/<int:id>/', views.eliminar_botin, name='eliminar_botin'),
    path('short/eliminar/<int:id>/', views.eliminar_short, name='eliminar_short'),
    
    
    path('busquedatipo/', views.busquedatipo, name='busquedatipo'),
    path('resultadobusqueda/', views.buscar, name='resultadobusqueda'),
]
