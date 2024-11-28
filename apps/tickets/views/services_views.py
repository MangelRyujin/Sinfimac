from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from apps.accounts.decorators import group_required
from apps.accounts.forms import *
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from apps.tickets.forms.service_form import *
from apps.tickets.models import Service 

# Create your views here.
@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def service_view(request):
    context={"services":Service.objects.exclude(is_delete=True)}
    return render(request, 'tickets/services/index.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def service_create(request):
    form=ServiceCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/servicios/')
    return render(request, 'tickets/services/actions/create.html', {'form': form})

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def service_edit(request,pk):
    service=Service.objects.filter(pk=pk,is_delete=False).first()
    if not service:
        return redirect('/servicios/')
    form = ServiceUpdateForm(instance=service)
    context={}
    if request.POST and service:
        form = ServiceUpdateForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            context['message']="Se ha editado correctamente"     
    context['form']=form
    context['service']=service
    return render(request, 'tickets/services/actions/edit.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def service_delete(request,pk):
    service=Service.objects.filter(pk=pk).first()
    service.is_delete=True
    service.save()
    return redirect('/servicios/')

 

