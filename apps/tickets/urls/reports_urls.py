from django.urls import path, include

from apps.accounts.views.general_views import *
from apps.tickets.views.reports_views import reports_view


urlpatterns = [
    path('', reports_view, name='reports'),
]