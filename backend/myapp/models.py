from django.db import models

# Create your models here.
class UserInput(models.Model):
    objective = models.TextField()

class Dataset(models.Model):
    user_input = models.ForeignKey(UserInput, on_delete=models.CASCADE)
    file = models.FileField(upload_to='datasets/')