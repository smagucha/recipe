from django.test import TestCase
from recipe.models import RecipeFood

class TestRecipeModels(TestCase):
	def test_RecipeFood(self):
		recipelabel= RecipeFood.objects.create(recipelabel='chicken')
		recipecalories = RecipeFood.objects.create(recipecalories= 124.556666)
		image_url = RecipeFood.objects.create(image_url='htpps://www.google.com')
		recipeingredient1=RecipeFood.objects.create(recipeingredient1=['dfk','jbdskfb'])

		self.assertEqual(str(recipelabel), 'chicken')