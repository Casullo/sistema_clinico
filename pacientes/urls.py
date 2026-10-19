from django.urls import path
from . import views

urlpatterns = [
       path('', views.listado_pacientes),
       path('buscar/', views.buscar),
       path('atencion/', views.detalle_atencion),
       path('<int:id>/', views.detalle_paciente),
   ]