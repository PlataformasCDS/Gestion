"""
from django import forms
from .models import OrdenCompra, ItemOrden
from django.forms.models import inlineformset_factory

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = '__all__'
        exclude = ['empresa', 'numero', 'estado']

ItemOrdenFormSet = inlineformset_factory(OrdenCompra, ItemOrden, fields=('cantidad', 'codigo', 'descripcion', 'valor_unitario'), extra=1)
"""