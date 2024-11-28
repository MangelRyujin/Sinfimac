from django import forms
from apps.tickets.models import Service


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['is_delete']
        
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['is_delete']