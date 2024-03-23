from django.db import models
from django.utils.timezone import now

class Seller(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    avatar = models.FileField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    img = models.ImageField()
    slug = models.CharField(max_length=130, default=None)
    datetime = models.DateTimeField(default=now)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

