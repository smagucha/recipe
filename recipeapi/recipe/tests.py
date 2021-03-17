from django.test import TestCase
from recipe.models import RecipeFood
from django.urls import reverse
from  recipe.views import home, searchform, Favoriterecipe
from django.urls import resolve

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')  
		self.assertEqual(found.func, home)

	def test_root_url_resolves_to_searchform_view(self):
		found = resolve('/search')  
		self.assertEqual(found.func, searchform)

	def test_root_url_resolves_to_Favoriterecipe_view(self):
		found = resolve('/favouriterecipe')  
		self.assertEqual(found.func, Favoriterecipe)


class TestRecipeModels(TestCase):
	def test_RecipeFood(self):
		recipelabel= RecipeFood.objects.create(recipelabel='chicken')
		recipecalories = RecipeFood.objects.create(recipecalories= 124.556666)
		image_url = RecipeFood.objects.create(image_url='htpps://www.google.com')
		recipeingredient1=RecipeFood.objects.create(recipeingredient1=['dfk','jbdskfb'])

		self.assertEqual(str(recipelabel), 'chicken')

# class TestUrl(TestCase):
# 	def test_checkhomeurl(self):
# 		response=self.client.get('/')
# 		self.assertEqual(response.status_code, 200)

	# def test_favouriterecipe(self):
	# 	response=self.client.get('/favouriterecipe')
	# 	self.assertEqual(response.status_code, 302)

	# def test_addrecipe(self):
	# 	response=self.client.get('/addrecipe')
	# 	self.assertEqual(response.status_code, 302)

	










