from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from apps.accounts.decorators import group_required
from apps.accounts.forms import RegisterForm, UserGestoreUpdateForm, UserTechnicalCreateForm,UserTechnicalUpdateForm
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from apps.accounts.models import Agency, User 

# Create your views here.
@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def users_view(request):
    context={"users":User.objects.exclude(
        Q(groups__name__in=["supervisor","gestor"]) | Q(is_delete=True)
    )}
    return render(request, 'accounts/users/index.html',context)


@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def user_detail_view(request,pk):
    context={"user":User.objects.get(pk=pk)}
    return render(request, 'accounts/users/user_detail.html',context)

@group_required('supervisor')
@login_required(login_url='/login/')
def user_gestora_create(request):
    form=RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            group=Group.objects.filter(name="gestor").first()
            if group:
                user.groups.add(group)
                user.save()
            return redirect('/usuarios/')
    return render(request, 'accounts/users/gestore/actions/create.html', {'form': form})

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def user_technical_create(request):
    form=UserTechnicalCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            group=Group.objects.filter(name="tecnico").first()
            if group:
                user.groups.add(group)
                user.save()
            return redirect('/usuarios/')
    return render(request, 'accounts/users/technical/actions/create.html', {'form': form,'agencies':Agency.objects.all()})

@group_required('supervisor')
@login_required(login_url='/login/')
def user_gestore_edit(request,pk):
    user=User.objects.get(pk=pk)
    form = UserGestoreUpdateForm(instance=user)
    context={}
    if request.POST and user:
        form = UserGestoreUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            context['message']="Se ha editado correctamente"     
    context['form']=form
    context['user']=user
    return render(request, 'accounts/users/gestore/actions/edit.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def user_technical_edit(request,pk):
    user=User.objects.get(pk=pk)
    form = UserTechnicalUpdateForm(instance=user)
    context={}
    if request.POST and user:
        form = UserTechnicalUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            context['message']="Se ha editado correctamente"     
    context['form']=form
    context['user']=user
    context['agencies']=Agency.objects.all()
    return render(request, 'accounts/users/technical/actions/edit.html',context)

@group_required('supervisor','gestor')
@login_required(login_url='/login/')
def user_delete(request,pk):
    user=User.objects.filter(pk=pk).first()
    user.is_delete=True
    user.is_active=False
    user.save()
    return redirect('/usuarios/')

 
