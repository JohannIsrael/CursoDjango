from django.shortcuts import render
from .models import Profesores

# Create your views here.
def home(request):
    
    profesores = Profesores.objects.all()
    
    for profesor in profesores:
        print(f'{profesor}, nombre_completo: {profesor.full_name(tipo='profesor')}')
        
    context = {
        'profesores':profesores
    }
    
    return render(request, 'home/pages/home.html', context)