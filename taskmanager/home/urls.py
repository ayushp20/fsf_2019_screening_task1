from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name =  'app-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name =  'task-detail'),
    path('task/new/', TaskCreateView.as_view(), name =  'task-create'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name =  'task-update'),
    path('about/', views.about, name = 'app-about'),

]