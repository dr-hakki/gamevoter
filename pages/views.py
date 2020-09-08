from django.shortcuts import render
from polls.models import Question, Choice, Application
from django import forms
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render, redirect

class NameForm(forms.Form):
    searched = forms.CharField(max_length=100)

def index(request):
  if request.method == "GET":
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    support = Application.objects.get(username="support")
    return render(request, 'pages/index.html',{"form": NameForm,"latest_question_list":latest_question_list,"support":support})
  else:
    try:
      latest_question_list = Question.objects.filter(question_text__icontains = request.POST["searched"])
      context = {'latest_question_list': latest_question_list}
      return render(request, 'polls/searchindex.html', context)
    except:
      latest_question_list = []
      context = {'latest_question_list': latest_question_list}
      return render(request, 'polls/searchindex.html', context)
      


