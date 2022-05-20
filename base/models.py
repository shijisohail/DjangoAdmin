from djongo import models
from django.contrib.auth.models import User
class Topics(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class CryptString(models.Model):
     HashString  = models.CharField(max_length=1000)
     def __str__(self):
         return self.HashString
#Checking git upload
class Blog(models.Model):
    hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
    name = models.CharField(max_length=255)
    description  = models.TextField(null=True,blank=True,max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
   
    def __str__(self):
     return self.name


class Machine (models.Model):   
     hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
     mach = models.FileField(null=True)
     cryptext = models.ForeignKey(CryptString,on_delete=models.SET_NULL,null=True)
     topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
     name = models.CharField(max_length=255)
     description  = models.TextField(null=True,blank=True,max_length=1000)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now=True)
     def __str__(self):
      return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE )
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[0:50]

