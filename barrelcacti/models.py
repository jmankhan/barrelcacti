from django.db import models

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