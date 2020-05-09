from django.db import models
from django.db import models
from django.utils.text import slugify

class Branch(models.Model):
    name        = models.CharField(max_length=255)
    address     = models.CharField(max_length=255)
    city        = models.CharField(max_length=255)
    timestamps  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)
