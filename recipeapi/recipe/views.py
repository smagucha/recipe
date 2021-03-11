from django.shortcuts import render
import requests
from .recipeapifolder import apikey
import json

def home(request):
	responseapi = requests.request("GET", apikey.url)
	r= responseapi.json()
	json_object = json.dumps(r)
	# hits=r['hits']
	recipe= r['hits'][0]['recipe']
	# recipelabel1=r['hits'][9]['recipe']['label']
	# recipeimage=r['hits'][9]['recipe']['image']
	# recipeingredientLines=r['hits'][9]['recipe']['ingredientLines']

	# for recipe in hits:
	# 	print('this is recipe  ...........', recipe['recipe'],  end='\n',)
	
	# for i in hits:
	# 	print(i['recipe']['label'], end='')
	# for r in recipe:
	# 	print(f"{r['recipe']['label']}- ingredients:{r['recipe']['ingredientLines'][0]}")
	# for r in recipe:
	# 	print(f"{r['recipe']['label']}- ingredients:{r['recipe']['ingredientLines']}")

	newrecipe=[]
	for i in recipe:
		newrecipeska={
			'recipelabel':r['hits'][0]['recipe']['label'],
			'recipeimage':r['hits'][0]['recipe']['image'],
			'recipeingredientLines':r['hits'][0]['recipe']['ingredientLines'][0],
		}
		newrecipe.append(newrecipeska)
	return render(request, 'recipe/home.html',{'newrecipe':newrecipe})
		

def Ingendrients(request):
	x =12345
	context={
	'y':x

	}
	return render(request, 'recipe/ingredientLines.html',context)