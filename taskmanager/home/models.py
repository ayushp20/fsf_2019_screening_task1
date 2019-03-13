from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

class Task(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	STATUS_CHOICES = (
		('Planned','Planned'),
		('In Progress', 'In Progress'),
		('Done', 'Done'),

	)

	status= models.CharField(max_length=100, choices=STATUS_CHOICES, default='Planned')
	

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('task-detail', kwargs={'pk':self.pk})