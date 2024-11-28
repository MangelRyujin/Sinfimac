from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from apps.accounts.decorators import user_is_not_authenticated
from apps.accounts.models import Agency
from apps.tickets.utils.reports import *
from ..forms import RegisterForm, UserPerfilGestoreUpdateForm, UserPerfilTechnicalUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    context={
        "new_tickets":new_tickets(),
        "proccess_tickets":proccess_tickets(),
        "expired_tickets":expired_tickets(),
        "confirm_tickets":confirm_tickets(),

    }
    return render(request, 'index.html',context)

@user_is_not_authenticated
def register(request):
    form=RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'register.html', {'form': form})

@user_is_not_authenticated
def user_login(request):
    context={
        "next": request.GET.get('next') or '/'
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url =  request.POST['next'] or '/'
        print(next_url)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'{next_url}')
        else:
            context['error']='Credenciales incorrectas!'
    return render(request, 'login.html',context)

@login_required(login_url='/login/')
def change_password_view(request):
    form=PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    context = {
        "form":form,
    }
    return render(request, 'accounts/change_password/change_password.html',context)

@login_required(login_url='/login/')
def change_perfil_view(request):
    if request.user.rol:    
        message=''
        if request.user.rol.name == "tecnico":
            form = UserPerfilTechnicalUpdateForm(instance=request.user)
        else:
            form = UserPerfilGestoreUpdateForm(instance=request.user)
        if request.method == 'POST':
            if request.user.rol.name == "tecnico":
                form = UserPerfilTechnicalUpdateForm(request.POST,instance=request.user)
            else:
                form = UserPerfilGestoreUpdateForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                message="Perfil editado correctamente"
        context = {
            "form":form,
            "agencies":Agency.objects.filter(is_delete=False),
            "message":message
        }
        return render(request, 'accounts/perfil/index.html',context)
    else:
        return redirect('/')