from apps.tickets.models import Ticket
from datetime import datetime,date, timedelta

def new_tickets():
    tickets = Ticket.objects.filter(state = "1")
    return tickets.count()

def proccess_tickets():
    tickets = Ticket.objects.filter(state = "2")
    return tickets.count()

def expired_tickets():
    fecha_actual = date.today()
    tickets = Ticket.objects.filter(state = "1")
    list = [ticket for ticket in tickets if ticket.created_date+timedelta(days=2) < fecha_actual]
    return list.__len__

def confirm_tickets():
    tickets = Ticket.objects.filter(state = "3")
    return tickets.count()