from django.urls import path, include

from apps.accounts.views.general_views import *


urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('cambiar-contraseña/',change_password_view,name='change_password_view'),
    path('mi-perfil/',change_perfil_view,name='change_perfil_view'),
]