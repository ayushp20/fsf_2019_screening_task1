from django.shortcuts import render
from .models import Task

def home (request):
	context = {
		'tasks': Task.objects.all()
	}
	return render (request, 'home/home.html', context)


def about(request):
	return render (request, 'home/about.html', {'title':'About'})
