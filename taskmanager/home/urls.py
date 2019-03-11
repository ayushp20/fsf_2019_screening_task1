from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name =  'app-home'),
    path('about/', views.about, name = 'app-about'),
]