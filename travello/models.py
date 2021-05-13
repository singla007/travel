from django.db import models

# Create your models here.
class student(models.Model):
    roll_id= models.IntegerField()
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    img= models.ImageField(upload_to="pics")
    class_name= models.CharField(max_length=100)
