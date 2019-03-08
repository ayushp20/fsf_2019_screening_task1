from django.shortcuts import render


tasks = [
	{
		'creator': 'CoreyMS',
		'title': 'Task 1',
		'content': 'first task content',
		'date_posted': 'March 8, 2019'
	}
]

def home (request):
	context = {
		'tasks': tasks
	}
	return render (request, 'home/home.html', context)


def about(request):
	return render (request, 'home/about.html', {'title':'About'})
