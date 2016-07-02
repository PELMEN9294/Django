from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def votes(request):
    return HttpResponse("You're voting on question %s." % question_text)

def detail(request, question_text):
    return HttpResponse("You're looking at question %s." % question_text)

def results(request, question_text):
    return HttpResponse("You're looking at the results of question %s." % question_text)
