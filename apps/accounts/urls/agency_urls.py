from django.urls import path
from apps.accounts.views.agency_views import *


urlpatterns = [
    path('', agency_view, name='agency'),
    path('detalle-de-agencia/<int:pk>/', agency_detail_view, name='agencyDetail'),
    path('crear-agencia/', agency_create, name='agencyCreate'),
    path('modificar-agencia/<int:pk>/', agency_edit, name='agencyEdit'),
    path('eliminar-agencia/<int:pk>/', agency_delete, name='agencyDelete')
    
]