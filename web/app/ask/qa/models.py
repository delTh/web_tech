from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models.User import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DataTimeField(blank=true)
	rating = models.IntegerField(11)
	author = ForegingKey(User)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DataTimeField(blank=true)
	question = ForegingKey(Question)
	author = ForegingKey(User)
