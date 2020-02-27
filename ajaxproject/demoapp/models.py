from django.db import models

# Create your models here.
#3. add models 
class stud(models.Model):
    rno = models.CharField(max_length=100)
    name =models.CharField(max_length=100)

    class Meta:
        db_table="student"     
    
