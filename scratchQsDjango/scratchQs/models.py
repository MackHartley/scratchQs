from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Community(models.Model):
	name = models.CharField(max_length=50, unique=True, default=None)
	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return 'Category: %s' % (self.name)

class Question(models.Model):
	community = models.ForeignKey(Community, on_delete=models.CASCADE, default=None)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	category = models.CharField(max_length=100)
	community = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return 'question: %s' % (self.title)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
	content = models.TextField()
	votes = models.IntegerField(default=0)
	# pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return 'Question: %s (Content: %s)' % (self.question, self.content)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class User(models.Model):
# 	community = models.ForeignKey(Community, on_delete=models.CASCADE, default=None)
# 	username = models.CharField(max_length = 50, unique = True)
# 	def __str__(self):
# 		return 'username: %s' % (self.name)
