from django import forms


class BibliotecasFormulario(forms.Form):
    
    ubicacion = forms.CharField(required=True)
    nroAsociados = forms.IntegerField()
    
    