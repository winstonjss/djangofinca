from django.db import models

# Create your models here.
class JhonatanSotelo(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    finca = models.CharField(max_length=100)
    hectareas = models.IntegerField()
    metros2 = models.IntegerField()
    propietario = models.CharField(max_length=100)
    cultivo = models.CharField(max_length=100)
def __str__(self):
    return self.id+''+self.finca+''+self.hectareas+''+self.metros2+''+self.propietario+''+self.cultivo