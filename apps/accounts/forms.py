from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import Agency, User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']

class UserTechnicalCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','is_active','first_name','last_name','agency','dni','birthdate','zone','shoe_size','polo_size','bank','yaple_plin','account','cci','password1','password2']
        

    
class UserGestoreUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','is_active','first_name','last_name']
        
class UserPerfilGestoreUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
        

class UserTechnicalUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','is_active','first_name','last_name','agency','dni','birthdate','zone','shoe_size','polo_size','bank','yaple_plin','account','cci']
        
        
class UserPerfilTechnicalUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','agency','dni','birthdate','zone','shoe_size','polo_size','bank','yaple_plin','account','cci']
        
        
class AgencyCreateForm(forms.ModelForm):
    class Meta:
        model = Agency
        exclude = ['is_delete']
        
class AgencyUpdateForm(forms.ModelForm):
    class Meta:
        model = Agency
        exclude = ['is_delete']