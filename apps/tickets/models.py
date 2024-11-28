from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator
from apps.accounts.models import Agency, User

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    is_delete=models.BooleanField(default=False)

    class Meta:
        verbose_name ="Service"
        verbose_name_plural ="Services"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    STATE_CHOICE = (
        ('1', 'atendida'),
        ('2', 'asignada'),
        ('3', 'confirmada'),
        ('4', 'denegada'),
    )
    SUB_STATE_CHOICE = (
        ('1', 'pendiente conformidad y registro confirmado'),
    )
    OBSERVATION_CHOICE = (
        ('1', 'SIN ASIGNAR'),
        ('2', 'ATS'),
        ('3', 'COMPLETO'),
        ('4', 'COTIZACION'),
        ('5', 'INFORME'),
    )
    
    code = models.CharField(max_length=50,unique=True)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE,related_name="agency_ticket")
    created_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_ticket")
    asigner_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_technical",null=True,blank=True)
    other = models.CharField(max_length=70)
    created_date = models.DateField(auto_created=True,auto_now_add=True)
    paid_date = models.DateField(auto_now_add=False,auto_created=False)
    materials_amount = models.DecimalField(max_digits=10,default=0,decimal_places=2,validators=[MinValueValidator(0)])
    passage_amount = models.DecimalField(max_digits=10,default=0,decimal_places=2,validators=[MinValueValidator(0)])
    labour_amount = models.DecimalField(max_digits=10,default=0,decimal_places=2,validators=[MinValueValidator(0)])
    deposit_amount = models.DecimalField(max_digits=10,default=0,decimal_places=2,validators=[MinValueValidator(0)])
    debt_amount = models.DecimalField(max_digits=10,default=0,decimal_places=2,validators=[MinValueValidator(0)])
    state = models.CharField(max_length=1,choices=STATE_CHOICE,default="1")
    sub_state = models.CharField(max_length=1,choices=SUB_STATE_CHOICE,default="1")
    observation = models.CharField(max_length=1,choices=OBSERVATION_CHOICE,default="1")
    description = models.TextField(max_length=500)
    payment=models.BooleanField(default=False)
    
    
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.code


class Facture(models.Model):
    CALIFICATION_CHOICE = (
        ('1', 'BUENO'),
        ('2', 'REGULAR'),
        ('3', 'MALO'),
    )
    code = models.CharField(max_length=50,unique=True)
    service = models.ForeignKey(Service,on_delete=models.PROTECT,related_name="services_facture")
    if_other = models.CharField(max_length=50,unique=True)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name="ticket_facture")
    description = models.TextField(max_length=500)
    other_description = models.TextField(max_length=500)
    calification = models.CharField(max_length=1,choices=CALIFICATION_CHOICE,default="1")

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
        return self.code