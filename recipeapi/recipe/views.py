from django.shortcuts import render
import requests
from .recipeapifolder import apikey
import json

def home(request):
	responseapi = requests.request("GET", apikey.url)
	r= responseapi.json()
	json_object = json.dumps(r)
	hits=r['hits']
	
	newrecipe=[]

	for recipe in hits:
		newrecipeska={
			'recipelabel':recipe['recipe']['label'],
			'recipeimage':recipe['recipe']['image'],
			'recipeingredientLines':recipe['recipe']['ingredientLines'],
		}
		newrecipe.append(newrecipeska)
	context ={
		'newrecipe':newrecipe
	}
	return render(request, 'recipe/home.html', context)
		

def Ingendrients(request):
	
	return render(request, 'recipe/ingredientLines.html',context)

def searchform(request):
	return render(request, 'recipe/search.html')
