from django.urls import path
from apps.accounts.views.users_views import *


urlpatterns = [
    path('', users_view, name='users'),
    path('detalle-de-usuario/<int:pk>/', user_detail_view, name='userDetail'),
    path('crear-gestora/', user_gestora_create, name='userGestoreCreate'),
    path('crear-tecnico/', user_technical_create, name='userTechnicalCreate'),
    path('modificar-usuario-gestore/<int:pk>/', user_gestore_edit, name='userGestoreEdit'),
    path('modificar-usuario-tecnico/<int:pk>/', user_technical_edit, name='userTechnicalEdit'),
    path('eliminar-usuario/<int:pk>/', user_delete, name='userDelete')
    
]