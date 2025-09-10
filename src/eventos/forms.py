from django import forms
from .models import EventosDB, OrganizadoresDB


class EventosForm(forms.ModelForm):
    class Meta:
        model = EventosDB
        fields = ['nombre', 'lugar']


class OrganizadoresForm(forms.ModelForm):
    class Meta:
        model = OrganizadoresDB
        fields = ['nombre', 'contacto']