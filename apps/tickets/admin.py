from django.contrib import admin

# Register your models here.

from apps.tickets.models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Ticket)
admin.site.register(Facture)
