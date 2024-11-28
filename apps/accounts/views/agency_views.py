from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from apps.accounts.decorators import group_required
from apps.accounts.forms import *
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from apps.accounts.models import Agency 

# Create your views here.
@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def agency_view(request):
    context={"agencies":Agency.objects.exclude(is_delete=True)}
    return render(request, 'accounts/agency/index.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def agency_detail_view(request,pk):
    context={"agency":Agency.objects.get(pk=pk)}
    return render(request, 'accounts/agency/agency_detail.html',context)


@group_required('supervisor','gestor')
def agency_create(request):
    form=AgencyCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/agencias/')
    return render(request, 'accounts/agency/actions/create.html', {'form': form})

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def agency_edit(request,pk):
    agency=Agency.objects.get(pk=pk)
    form = AgencyUpdateForm(instance=agency)
    context={}
    if request.POST and agency:
        form = AgencyUpdateForm(request.POST, instance=agency)
        if form.is_valid():
            form.save()
            context['message']="Se ha editado correctamente"     
    context['form']=form
    context['agency']=agency
    return render(request, 'accounts/agency/actions/edit.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def agency_delete(request,pk):
    agency=Agency.objects.filter(pk=pk).first()
    agency.is_delete=True
    agency.save()
    return redirect('/agencias/')

 

