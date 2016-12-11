from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Answer, Question, Community
import json
from django.template import loader

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'scratchQs/index.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'communities': Community.objects.all(),
        })
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-votes")


# def index(request):
# 	#pre load data
# 	context = {Question.objects.all()}
# 	# print(len(questions))
# 	# questionList = []
# 	# questionList.append(q1)
# 	# questionList.append(q2)
# 	# context = {"questions" : questionList}
# 	# context = 
# 	# print(context)
# 	# questionList = []
# 	# questions = Question.objects.all()
# 	# print(len(questions))
# 	# for question in questions:

# 	# 	question_context = {"title":question.title, "content": question.content, "votes":question.votes,
# 	# 		"category": question.category, "id" : question.pk}
# 	# 	questionList.append(question_context)
# 	# context = {"questions" : questionList}
# 	return render(request, "scratchQs/index.html", context)


def answers(request,question_id):
	parent_question = Question.objects.get(pk=question_id)
	answers = Answer.objects.filter(question_id=question_id)
	answers = answers.order_by("-votes")
	context = {"title" : parent_question.title, "content":parent_question.content,"answers" : answers, 'communities': Community.objects.all()}
	return render(request,"scratchQs/answer_page.html", context)



# #The next functions all expect POST requests
def community_questions(request, community_id):
	parent_community = Community.objects.get(pk=community_id)
    #print(parent_community.name)
    #print(Question.objects.filter(community=parent_community.name))
	
	filtered_questions = Question.objects.filter(community=parent_community.name)
 	context = {"questions": filtered_questions, 'communities': Community.objects.all()}

 	return render(request,"scratchQs/index.html",context)

# The next functions all expect POST requests
@csrf_exempt
def upvote_question(request):
	parent_question_id = request.POST.get("question_id")
	print(parent_question_id)
	parent_question = Question.objects.get(pk=parent_question_id)
	parent_question.votes = parent_question.votes+1
	parent_question.save()
	response = {"status" : 200, "question_id" : parent_question.pk, "title":parent_question.title, "content": parent_question.content, "votes": parent_question.votes}
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def downvote_question(request):
	parent_question_id = request.POST.get("question_id")
	print(parent_question_id)
	parent_question = Question.objects.get(pk=parent_question_id)
	parent_question.votes = parent_question.votes-1
	parent_question.save()
	response = {"status" : 200, "question_id" : parent_question.pk, "title":parent_question.title, "content": parent_question.content, "votes": parent_question.votes}
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def upvote_answer(request):
	parent_answer_id = request.POST.get("answer_id")
	print(parent_answer_id)
	parent_answer = Answer.objects.get(pk=parent_answer_id)
	parent_answer.votes = parent_answer.votes+1
	parent_answer.save()
	response = {"status" : 200, "answer_id" : parent_answer.pk, "content": parent_answer.content, "votes": parent_answer.votes}
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def downvote_answer(request):
	parent_answer_id = request.POST.get("answer_id")
	print(parent_answer_id)
	parent_answer = Answer.objects.get(pk=parent_answer_id)
	parent_answer.votes = parent_answer.votes-1
	parent_answer.save()
	response = {"status" : 200, "answer_id" : parent_answer.pk, "content": parent_answer.content, "votes": parent_answer.votes}
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def add_question(request):
	if request.method == "POST":
		questionTitle = request.POST.get("title")
		questionContent = request.POST.get("content")
		questionCategory = request.POST.get("category")
		newQuestion = Question(title=questionTitle,content=questionContent,category=questionCategory)
		newQuestion.save()
		response = {"status" : 200, "title":newQuestion.title, "content": newQuestion.content, "category": newQuestion.category}
		return HttpResponse(json.dumps(response), content_type="application/json")
	else:
		return HttpResponse("failure")
	# return HttpResponse(json.dumps(response), content_type="application/json")

# @csrf_exempt
# def add_answer(request):
# 	# questionId = request.POST.get("question_id")
# 	answerText = request.POST.get("answer_text")
# 	question = Question.objects.get(pk=questionId)
# 	newAnswer = Answer(question, answerText) #Should we assume someone adding an answer is a vote
# 	newAnswer.save()
# 	response = {"status" : 200, "answer_text" : answerText}
# 	return HttpResponse(json.dumps(response), content_type="application/json")

def signup(request):
	return render(request, "scratchQs/signup.html", {})


