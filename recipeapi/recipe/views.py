from django.shortcuts import render
import requests
import json
from django.http import HttpResponseRedirect
import os
from django.contrib.auth.decorators import login_required
from .models import RecipeFood
from .forms import RecipeForm

@login_required(login_url='/accounts/login/')
def home(request):
	return render(request, 'recipe/search.html')

	

		
@login_required(login_url='/accounts/login/')
def Favoriterecipe(request):
	allfavour=RecipeFood.objects.all()
	return render(request, 'recipe/favoriterecipe.html',{'allfavour':allfavour})
	
@login_required(login_url='/accounts/login/')
def searchform(request):
	if request.user.is_authenticated:#user.is_authenticated
		id_app=os.environ.get('id_app')  
		Api_key=os.environ.get('Api_key')
		values=request.POST.get('q','')
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
	else:
		return HttpResponseRedirect('login')


@login_required(login_url='/accounts/login/')
def addrecipe(request):
	if request.method =='POST':
		form =  RecipeForm(request.POST)
		if form.is_valid():
			form.save()
			form =  RecipeForm()
			return HttpResponseRedirect('favouriterecipe')
	else:
		form =  RecipeForm()
		return render(request, 'recipe/addrecipe.html', {'form': form})
