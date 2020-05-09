from django.db import models
from django.utils.text import slugify

class Menu(models.Model):
    name        = models.CharField(max_length=255)
    image       = models.TextField(blank=True)
    description = models.TextField()
    price       = models.CharField(max_length=255)
    category    = models.TextField(max_length=50, default="Uncategorized")
    catslug     = models.SlugField(editable=False)
    timestamps  = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.catslug = slugify(self.category)
        super(Menu, self).save()

    def __str__(self):
        return "{}".format(self.name)