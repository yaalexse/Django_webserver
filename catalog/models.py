from django.db import models
from django.urls import reverse
import uuid
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

class Codes(models.Model):

	code_id = models.UUIDField(primary_key =True, default=uuid.uuid4)
	
	author_id = models.ForeignKey('new_Authors', on_delete=models.SET_NULL, null=True)
	
	title = models.CharField(max_length = 255, help_text = 'Write a brief name for the code')
	
	language = models.CharField(max_length=50)
	
	content = models.TextField()
	
	description = models.TextField(help_text = 'Write a small but usefull description for you and other user understanding')
	
	timestamp = models.DateField(auto_now=True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('code-detail',args=[str(self.code_id)])

	def get_author_name(self):

		return self.author_id
		
'''
class Authors(models.Model):

	author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= 'Unique ID for users')

	user_name= models.CharField(max_length=20,unique=True)

	password = models.CharField(max_length=200)
	
	email = models.EmailField()
	
	join_date = models.DateField(auto_now=True)
	
	job = models.CharField(max_length=100)
	
	job_description = models.TextField()
	
	class Meta:
		ordering = ['user_name','job']
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('author-detail',args=[str(self.id)])
'''

class new_Authors(models.Model):

	name = models.ForeignKey(User, on_delete=models.CASCADE)
	
	password = models.CharField(max_length=200)
	
	email = models.EmailField()
	
	join_date = models.DateField(auto_now=True)
	
	job = models.CharField(max_length=100)
	
	job_description = models.TextField()
	
	class Meta:
		ordering = ['name','job']
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('author-detail',args=[str(self.name)])