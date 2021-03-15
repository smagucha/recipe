from .models import RecipeFood
from django.forms import ModelForm

class RecipeForm(ModelForm):
	class Meta:
		model = RecipeFood
		fields='__all__'