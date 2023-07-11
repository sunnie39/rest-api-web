from django.db import models

# Create your models here.

#class Item(models.Model):
 #   name = models.CharField(max_length=100)
  #  description = models.TextField(max_length=300)
  #  cost = models.IntegerField()

class Post(models.Model):
    
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()             # content 컬럼
    writer = models.CharField(null=True,default='',max_length=200) # writer 컬럼

    def __str__(self):
        """A string representation of the model."""
        return self.title