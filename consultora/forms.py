from django import forms
from .models import *

class PostulanteCrearForm(forms.ModelForm):

    fechanacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Nacimiento')
    documento = forms.ChoiceField(
        choices=[(x.id,x.tipo) for x in Documento.objects.all()]
         )

    def save(self, commit=True):
      instance = super().save(commit=False)
      doc = self.cleaned_data['documento']
      instance.publication = Documento.objects.get(pk=doc)
      instance.save(commit)
      return instance
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
    
    
    class Meta:
        model = BusquedaLaboral
        fields = '__all__'
    
    
    
    
    

