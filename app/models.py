from django.db import models

from django import forms
# Create your models here.


class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(default='abc')
    text=models.CharField(max_length=700,default='enter text')

    def __str__(self):
        return self.name
    


# class Feedback(models.Model):
#     name=models.CharField(max_length=200,required = True)
#     email=models.EmailField(default='abc',required = True)
#      text=models.CharField(max_length=700,default='enter text',required = True) 