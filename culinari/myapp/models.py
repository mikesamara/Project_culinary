from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)





class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, default='Другие')

    def __str__(self):
        return self.name


class Recipe(models.Model):

    name_recipe = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    ingredients = models.TextField()
    steps_cooking = models.TextField(blank=False)
    time_cooking = models.TextField(blank=False)
    image = models.FileField(upload_to= 'files/', blank=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    data_add = models.DateTimeField(auto_now_add=True)
    category_recipe = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_recipe, self.ingredients, self.time_cooking, self.data_add

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:10])}'

     def get_steps(self):
        words = self.steps_cooking.split()
        return f'{" ".join(words[:50])}'





# Create your models here.
