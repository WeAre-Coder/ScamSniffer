from django.db import models

# Create your models here.

class Link(models.Model):

    def __str__(self):  #to display the link name directly instead of "link(1)"
        return self.link

    link = models.CharField(max_length=5000)
    status = models.CharField(max_length=100)
