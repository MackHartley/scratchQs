from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	category = models.charField(max_length=100)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return 'question: %s' % (self.title)

class Answer(models.Model):
	content = models.TextField()
	votes = models.IntegerField(default=0)