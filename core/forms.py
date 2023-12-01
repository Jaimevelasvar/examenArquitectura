from django import forms
from .models import *

class formTransaccion(forms.ModelForm):
    destino = forms.CharField(max_length=30)
    ropa = forms.ModelChoiceField(Ropa.objects.all(), label='Seleccione tipo de ropa')
    cantidad = forms.IntegerField()
    opciones = (
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso')
    )
    tipo_transaccion = forms.ChoiceField(choices=opciones)
    opciones2 = (
        ('Limpia', 'Limpia'),
        ('Sucia', 'Sucia')
    )
    estado_ropa = forms.ChoiceField(choices=opciones2)
    class Meta():
        model = Transaccion
        fields = ("destino", "ropa" ,"cantidad", "tipo_transaccion", "estado_ropa")

        
