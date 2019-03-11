from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name =  'app-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name =  'task-detail'),
    path('about/', views.about, name = 'app-about'),
]