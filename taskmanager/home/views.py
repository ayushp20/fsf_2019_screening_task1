from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

def home (request):
	context = {
		'tasks': Task.objects.all()
	}
	return render (request, 'home/home.html', context)


class TaskListView(ListView):
	model = Task
	template_name = 'home/home.html'
	context_object_name = 'tasks'
	ordering = ['-date_posted']


class TaskDetailView(DetailView):
	model = Task



def about(request):
	return render (request, 'home/about.html', {'title':'About'})


