from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title= models.CharField(max_length=125)
    content= models.TextField()
    author= models.CharField(max_length=13)
    slug= models.CharField(max_length=13)
    timeStamp=models.DateTimeField()
    def __str__(self):
        return self.title + ' by ' + self.author
