from django.db import models

# Create your models here.
class Users(models.Model):
    
    name=models.CharField(max_length=30)
    mobile_no=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=10)
   
    def __str__(self):
        return self.name
    

class Todolist(models.Model):

    user_id=models.CharField(max_length=10)
    title=models.CharField(max_length=50)
    tags=models.TextField()
    time=models.TextField()
    date=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    status=models.TextField()
    


    def __str__(self):
        return self.title


