from django import forms
from .models import *

class PostulanteCrearForm(forms.ModelForm):

    fechanacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Nacimiento')
    class Meta:
        model = Postulante
        fields = '__all__'
    

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
    tecnologia = forms.ModelMultipleChoiceField(queryset=Tecnologia.objects.all())

    def save(self, commit=True):
       instance = super().save(commit=False)
       tec = self.cleaned_data['tecnologia']
       instance.tecnologia = tec[0]
       instance.save(commit)
       return instance

    class Meta:
        model = BusquedaLaboral
        fields = '__all__'
    
    
    
    
    

