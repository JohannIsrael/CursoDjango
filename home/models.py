from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aulas(models.Model):
    nombre = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'aulas'
        
    def __str__(self):
        return self.nombre

    
class Carreras(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'carreras'
    
        
class Alumnos(models.Model):
    
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_carrera = models.OneToOneField(Carreras, on_delete=models.PROTECT)
    id_carrera = models.ForeignKey(Aulas, on_delete=models.PROTECT)
    semestre = models.IntegerField()
    
    class Meta:
        db_table = 'alumnos'
        
    def __str__(self):
        return f'{self.id_user.username} semetre: {self.semestre}'
    
class Materias(models.Model):
    
    nombre = models.CharField(max_length=100)
    id_carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'materias'

class Profesores(models.Model):
    
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_aula = models.OneToOneField(Aulas, on_delete=models.CASCADE)
    id_materias = models.OneToOneField(Materias, on_delete=models.CASCADE)
    
    class Meta:      
        db_table = 'profesores'
        
    def __str__(self) -> str:
        return f'{self.id_user.username}/{self.id_user.id}'
    
    def full_name(self, *args, **kwargs):
        
        tipo = kwargs.get('tipo')
                
        return f'{self.id_user.first_name} {self.id_user.last_name}, tipo={tipo}'
        