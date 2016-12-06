from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=200, unique=True)
	question_content = models.TextField()
	category = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return 'question: %s' % (self.title)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_content = models.TextField()
	votes = models.IntegerField(default=0)

	def __str__(self):
		return 'answer: %s %s' % (self.answer_content, self.question.title)