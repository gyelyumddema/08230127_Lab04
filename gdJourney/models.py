from django.db import models

# Create your models here.
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_learned = models.DateField()
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    
    def __str__(self):
        return self.name
    
class ProjectDocumentation(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='documentation/')
    
    def __str__(self):
        return self.title