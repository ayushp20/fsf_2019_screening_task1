from django.shortcuts import render
from .models import Task
from django.views.generic import ListView

def home (request):
	context = {
		'tasks': Task.objects.all()
	}
	return render (request, 'home/home.html', context)


class PostListView(ListView):
	model = Task
	template_name = 'home/home.html'
	context_object_name = 'tasks'

def about(request):
	return render (request, 'home/about.html', {'title':'About'})


