from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Questions

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'votes/index.html', context)


def votes(request):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(question, 'votes/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)
