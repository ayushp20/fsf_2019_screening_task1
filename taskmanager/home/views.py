from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class TaskCreateView( LoginRequiredMixin, CreateView):
	model = Task
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class TaskUpdateView( LoginRequiredMixin, UpdateView):
	model = Task
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

def about(request):
	return render (request, 'home/about.html', {'title':'About'})


