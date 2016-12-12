from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Answer, Question, Community
import json
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
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


def answers(request,question_id):
	parent_question = Question.objects.get(pk=question_id)
	answers = Answer.objects.filter(question_id=question_id)
	answers = answers.order_by("-votes")
	context = {"question": parent_question, "title" : parent_question.title, "content":parent_question.content,"answers" : answers, 'communities': Community.objects.all()}
	return render(request,"scratchQs/answer_page.html", context)


def search_question(request,search_text):
	question_text = search_text
	if question_text is not None:            
		#results = Question.objects.filter(title=question_text)
		results = Question.objects.filter(title__contains=question_text)
		context = {"questions": results, 'communities': Community.objects.all()}
		return render(request,"scratchQs/index.html",context)


def community_questions(request, community_id):
	parent_community = Community.objects.get(pk=community_id)
    #print(parent_community.name)
    #print(Question.objects.filter(community=parent_community.name))
	
	filtered_questions = Question.objects.filter(community=parent_community.name).order_by("-votes")
 	context = {"questions": filtered_questions, 'communities': Community.objects.all()}

 	return render(request,"scratchQs/index.html",context)



def order_by_answers(request, community_id):
	parent_community = Community.objects.get(pk=community_id)
    #print(parent_community.name)
    #print(Question.objects.filter(community=parent_community.name))
	
	filtered_questions = Question.objects.filter(community=parent_community.name).order_by("votes")
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

@csrf_exempt
def add_answer(request):
	if (request.POST and request.POST['parentQuestionID'] and request.POST['content']):
		parentQuestionID = request.POST['parentQuestionID']
		content = request.POST['content']
		foreignParentObject = Question.objects.filter(id = parentQuestionID)[0]
		newAnswer = Answer(question = foreignParentObject, content = content)
		newAnswer.save()
		return HttpResponse(json.dumps({'status': 200}), content_type = 'application/json')
	else:
		return HttpResponse('failure: add_answer in views.py')


def signup(request):
	return render(request, "scratchQs/signup.html", {})


