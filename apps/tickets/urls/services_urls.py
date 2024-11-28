from django.urls import path
from apps.tickets.views.services_views import *


urlpatterns = [
    path('', service_view, name='service'),
    path('crear-servicio/', service_create, name='serviceCreate'),
    path('modificar-servicio/<int:pk>/', service_edit, name='serviceEdit'),
    path('eliminar-servicio/<int:pk>/', service_delete, name='serviceDelete')
    
]