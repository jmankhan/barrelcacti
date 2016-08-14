from django.db import models
from tinymce import models as tinymce_models
import random

class Album(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	img = models.CharField(max_length=200)
	release_date = models.DateField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Track(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	length = models.TimeField()

	def __unicode__(self):
		return self.title
		
	def __str__(self):
		return self.title;

class Member(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	role = models.CharField(max_length=300)
	bio = tinymce_models.HTMLField()

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Story(models.Model):
	title = models.CharField(max_length=30)
	text = tinymce_models.HTMLField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Image(models.Model):
	# image = models.ImageField(upload_to = 'gallery/', default = 'gallery/unknown/' + repr(random.random()) + '.jpg')
	name = models.CharField(max_length=30)
	
