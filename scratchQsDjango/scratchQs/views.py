from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Answer, Question
import json


# Create your views here.

# class Question(models.Model):
# 	title = models.CharField(max_length=200, unique=True)
# 	content = models.TextField()
# 	category = models.charField(max_length=100)
# 	votes = models.IntegerField(default=0)
# 	def __str__(self):
# 		return 'question: %s' % (self.title)


def questions(request):
	

