from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.forms.models import model_to_dict  
import json, time
from web.Table import Table
from web import settings
		
def home(request) :
	return render_to_response('home.html', locals())

def show_table(request) :
	settings.table.next_generation()
	return HttpResponse(settings.table.show_table())

def new_random_table(request) :
	settings.table = Table(height = 7, weight = 7)
	return HttpResponse("200")

def new_input_table(request) :
	print request.GET.get("input_table")
	with open("../test_case/test_case_temp", 'w') as f:
		f.write(request.GET.get("input_table"))
	settings.table = Table(file_path="../test_case/test_case_temp")
	return HttpResponse("200")
