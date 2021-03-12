from django.shortcuts import render
import requests
import json
from django.http import HttpResponseRedirect
import os

def home(request):
	id_app=os.environ.get('id_app')  
	Api_key=os.environ.get('Api_key')
	values=request.POST.get('q',default=None)
	print(values)
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
