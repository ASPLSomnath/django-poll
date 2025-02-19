from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse

from .models import Choice, Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")

    return render(request , "polls/index.html", {'latest_question_list' : latest_question_list})


def detail(request, question_id):
    try :
        question = Question.objects.get(pk = question_id)

    except Question.DoesNotExist :
        raise Http404("Question does not exist")
    
    return render(request , "polls/detail.html" , {"question":question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
