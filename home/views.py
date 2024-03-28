from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesores, Carreras, Alumnos
from .forms import Form, FormCarreras, FormRegister
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    
    """Manejando QuerySETS más ejemplos:  https://docs.djangoproject.com/en/5.0/ref/models/querysets/"""
    
    profesores = Profesores.objects.all()   
    carrera_sistemas = Carreras.objects.filter(nombre='Sistemas')
    
    carrera = Alumnos.objects.filter(id=2)
    print(carrera.first().semestre)

    print(type(carrera_sistemas))
    
    if(len(carrera_sistemas)> 0):
        print('Obtuve un resultado')
        
    alumno = get_object_or_404(Alumnos, id=2)
    print(alumno.semestre)
    # print(type(alumno))
    
    """Instancia de los elementos de de un Modelo"""
    
    for profesor in profesores:
        print(f'{profesor}, nombre_completo: {profesor.full_name(tipo='profesor')}')
    
    form = Form()
    form_carrareras = FormCarreras()
    
    if request.POST:
        # print(request.POST)
        # print(request.POST.get("nombre"))
        
        form_carrareras = FormCarreras(request.POST)
        
        if form_carrareras.is_valid():
            
            data = form_carrareras.save(commit=False)
            print(data.nombre)
            
            carrera = Carreras(nombre=data.nombre)
            carrera.save()
            
            redirect('home.Home')
        else:
            print(form_carrareras.errors)
        
    context = {
        # 'profesores':profesores
        'form':form,
        'form_carreras':form_carrareras
    }
    
    return render(request, 'home/pages/home.html', context)

def view_register(request):
    
    msj = None
    msj_type= None
    form = FormRegister()
    
    if request.POST:
        
        form = FormRegister(request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            email = request.POST.get('email','')
            password = request.POST.get('password')
            msj = 'Register Succees!'
            msj_type = 'success'
            User.objects.create_user(username, email, password)
        else:
            
            msj = 'Failed Register!'
            msj_type = 'danger'
        
    context = {
        'form': form,
        'msj':msj,
        'msj_type':msj_type
    }
    
    return render(request, 'home/pages/register.html', context)