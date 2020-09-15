from django.db import models

# Create your models here.
class Task(models.Model):
    singleTask = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.singleTask
    