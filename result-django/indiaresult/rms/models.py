from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    father_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    english = models.IntegerField()
    hindi = models.IntegerField()
    
    def __str__(self):
        return self.name