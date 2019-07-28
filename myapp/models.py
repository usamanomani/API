from django.db import models

# Create your models here.
class Users(models.Model):
    fname =models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.TextField()
    email =models.EmailField(unique=True)

    def __str__(self):
        return self.fname