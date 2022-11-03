from django import forms
from .models import *

class PostulanteCrearForm(forms.ModelForm):

    fechanacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Nacimiento')
    documento = forms.ModelChoiceField(queryset=Documento.objects.all())

    class Meta:
        model = Postulante
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['documento'] = kwargs['instance'].groups.all()[0]
            else:
                initial['documento'] = None
        forms.ModelForm.__init__(self, *args, **kwargs)


    

class PostulanteSearchForm(forms.ModelForm):
   class Meta:
     model = Postulante
     fields = ['nombre', 'apellido']

class IdiomaForm(forms.ModelForm):   

    class Meta:
        model = PostulanteIdioma
        fields = '__all__'

class OrganizacionSearchForm(forms.ModelForm):
   class Meta:
     model = Organizacion
     fields = ['razonsocial']

class OrganizacionForm(forms.ModelForm):   
    
    class Meta:
        model = Organizacion
        fields = '__all__'

    barrio = forms.ModelChoiceField(queryset=Barrio.objects.all())

class BusquedaLaboralForm(forms.ModelForm):   

    fechaApertura = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Apertura')
    fechaCierre = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Cierre')
    
    
    class Meta:
        model = BusquedaLaboral
        fields = '__all__'
    
    
    
    
    

