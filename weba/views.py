from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def web1(request):
    # return HttpResponse("hello!,ok")
    res = []
    for i in Question.objects.all():
        res.append(i.question_text)
    # return HttpResponse(res)
    return render(request, "./weba/index.html", {"dd": res})


def getChoices(request, question_id):
    print(question_id)
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    for i in choices:
        print(i.choice_text)
    return render(request, "./weba/choices.html", {"dd": choices})


def login(request):
    return render(request, "./weba/login.html", {})


def status(request):
    print(request.GET)
    return render(request, "weba/status.html", {})
