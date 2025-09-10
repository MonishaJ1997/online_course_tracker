from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    progress = models.IntegerField(default=0)  # percentage

    def __str__(self):
        return self.title
