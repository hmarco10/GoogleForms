from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creando modelos

class Post(models.Model):
    User = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    GoogleForm = models.CharField(max_length=150,default="")
    description = models.CharField(max_length=350,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.GoogleForm

class Questions(models.Model):
    GoogleForm = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=150, null=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Questions,null=True, blank=True, on_delete=models.CASCADE)
    #answer = models.IntegerField(default=0)
    answer = models.CharField(max_length=50,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.answer
    
    
        