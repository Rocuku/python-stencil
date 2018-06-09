from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.forms.models import model_to_dict  
import json, time
from Table import Table
from Cell import Cell
from web import settings
		
def home(request) :
	return render_to_response('home.html', locals())

def show_table(request) :
	settings.table.next_generation()
	return HttpResponse(settings.table.show_table())

def new_random_table(request) :
	settings.table = Table(height = 3, weight = 3)
	return HttpResponse("200")

