from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):    
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
            )
        #Se utiliza para personalizar los elementos del form, 'titulo' es el campo a personalizar
        # 'forms.TextInput' tipo de elemento, en 'attrs' van los atributos que irian en la etiqueta html
        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese texto aquí',
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
        

