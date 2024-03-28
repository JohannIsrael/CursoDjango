from django import forms
from .models import Carreras

class Form(forms.Form):
    
    """Formulario Genérico"""
    
    nombre = forms.CharField()
    edad = forms.IntegerField()

class FormCarreras(forms.ModelForm):
    
    """Formulario Instanciando de un modelo"""
    
    # nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'prueba'}))
    
    class Meta:
        
        model = Carreras
        fields = '__all__'
        
        widgets = {
            "nombre": forms.TextInput(attrs={'required':''}),
        }
        
    def __init__(self, *args, **kwargs):
        super(FormCarreras, self).__init__(*args, **kwargs)
        # self.fields['nombre'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class FormRegister(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField(required=False)
    passsword = forms.CharField(widget = forms.TextInput(attrs={'type':'password'}))
    
    def __init__(self, *args, **kwargs):
        super(FormRegister, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        