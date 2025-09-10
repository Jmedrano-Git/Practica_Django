from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_eventos, name="lista_evento"),
    path('nuevo/', views.crear_eventos, name="crear_evento"),
    path('editar/<int:pk>/', views.editar_evento, name="editar_evento"),
    path('eliminar/<int:pk>/', views.eliminar_evento, name="eliminar_evento"),
    path('asignar-tarea/<int:pk>/', views.asignar_organizador, name="asignar_organizador"),
    path('tarea/toggle/<int:tarea_id>/', views.toggle_Organizador, name='toggle_organizador'),
]
