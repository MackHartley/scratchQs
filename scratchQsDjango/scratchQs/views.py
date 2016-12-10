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


#class Answer(models.Model):
#	content = models.TextField()
#	votes = models.IntegerField(default=0)

def questions(request):
	#pre load data
	q1 = Question(title="title 1", content="content 1", pk=0)
	q2 = Question(title="title 2", content="content 2", pk=1)
	q1.save()
	q2.save()
	questions = Question.objects.all()
	print(len(questions))
	questionList = []
	questionList.append(q1)
	questionList.append(q2)
	context = {"questions" : questionList}
	print(context)
	# questionList = []
	# questions = Question.objects.all()
	# print(len(questions))
	# for question in questions:

	# 	question_context = {"title":question.title, "content": question.content, "votes":question.votes,
	# 		"category": question.category, "id" : question.pk}
	# 	questionList.append(question_context)
	# context = {"questions" : questionList}
	return render(request, "scratchQs/index.html", context)

# def answer(request,question_id):
# 	question = Question.objects.get(pk=question_id)
# 	answers = Answer.objects.filter(question_id=question_id)
# 	context = {"title" : question.question_title, "answers" : answers}
# 	return render(request,"answer_page.html", context)

# #The next functions all expect POST requests
def add_question(request):
	questionTitle = request.POST.get("title")
	questionContent = request.Post.get("content")
	newQuestion = Question(questionTitle,questionContent)
	newQuestion.save()
	response = {"status" : 200, "question_id" : newQuestion.pk, "title":question.title, "content": question.content}
	return HttpResponse(json.dumps(response), content_type="application/json")


# def add_answer(request):
# 	questionId = request.POST.get("question_id")
# 	answerText = request.POST.get("answer_text")
# 	question = Question.objects.get(pk=questionId)
# 	newAnswer = Answer(question, answerText) #Should we assume someone adding an answer is a vote
# 	newAnswer.save()
# 	response = {"status" : 200, "answer_id" : newAnswer.pk, "answer_text" : answerText}
# 	return HttpResponse(json.dumps(response), content_type="application/json")



	

