from django.db import models
from django.contrib.postgres.fields import ArrayField

class RecipeFood(models.Model):
	recipelabel= models.CharField(max_length=100)
	recipeimage = models.ImageField(upload_to='imagerecipe',  null =True, blank=True)
	image_url = models.URLField(max_length=200, null =True, blank=True)
	recipeingredient1=ArrayField(models.CharField(max_length=200), blank=True, null= True)




