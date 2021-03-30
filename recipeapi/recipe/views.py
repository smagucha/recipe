from django.shortcuts import render
import requests
import json
from django.http import HttpResponseRedirect
import os
from django.contrib.auth.decorators import login_required
from .models import RecipeFood
from decouple import config

@login_required(login_url='/accounts/login/')
def home(request):
	# print('this is the status',status_code)
	return render(request, 'recipe/search.html')

@login_required(login_url='/accounts/login/')
def Favoriterecipe(request):
	allfavour=RecipeFood.objects.all()
	return render(request, 'recipe/favoriterecipe.html',{'allfavour':allfavour})
	
@login_required(login_url='/accounts/login/')
def searchform(request):
	id_app=config('id_app')  
	Api_key=config('Api_key')
	values=request.POST.get('q','')
	url='https://api.edamam.com/search?q='+values+'&app_id='+ id_app +'&app_key='+Api_key+''
	responseapi = requests.request("GET", url)
	r= responseapi.json()
	json_object = json.dumps(r)
	hits=r['hits']

	newrecipe=[]

	for recipe in hits:
		newrecipeska={
			'recipelabel':recipe['recipe']['label'],
			'recipeimage':recipe['recipe']['image'],
			'recipeingredientLines':recipe['recipe']['ingredientLines'],
			'recipecalories':recipe['recipe']['calories'],
		}

		newrecipe.append(newrecipeska)

	# for recipe in hits:
	# 	recipe_save= RecipeFood.objects.create(
	# 	recipelabel=recipe['recipe']['label'],
	# 	recipecalories =recipe['recipe']['calories'],
	# 	image_url =recipe['recipe']['image'],
	# 	recipeingredient1 =recipe['recipe']['ingredientLines']
	# 	)
	# 	recipe_save.save()
	context ={
		'newrecipe':newrecipe,
		#'recipe_save':recipe_save,
	}

	return render(request, 'recipe/home.html', context)







