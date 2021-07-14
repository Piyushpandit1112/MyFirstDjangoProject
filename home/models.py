from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=122)
    zip = models.CharField(max_length=6)
    desc = models.TextField()
    date = models.DateField()
 
    # For changing Object1 to real name
    def __str__(self):
        return self.name
    

