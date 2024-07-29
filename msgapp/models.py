from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=20)
    mob=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    msg=models.CharField(max_length=300)

# class name =table name 
# class datamemebers = column in table
# class object = Recordes in table
