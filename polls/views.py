from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Question, Choice

# Get questions and display them
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def indexaction(request):
    latest_question_list = Question.objects.filter(category="action")
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def indexstrategy(request):
    latest_question_list = Question.objects.filter(category="strategy")
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  if question.choice_number == 2:
      return render(request, 'polls/results2.html', { 'question': question })
  elif question.choice_number == 3:
      return render(request, 'polls/results3.html', { 'question': question })
  elif question.choice_number == 4:
      return render(request, 'polls/results4.html', { 'question': question })
  elif question.choice_number == 5:
      return render(request, 'polls/results5.html', { 'question': question })
  

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    myuser = request.user

    if myuser in question.vdq.all():
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You voted for this before.",
            })
    else:
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            question.vdq.add(myuser)
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)


def signupuser(request):
    if request.method == "GET":
        return render(request,"pages/signupuser.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:

                user = User.objects.create_user(request.POST["username"], password= request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("/")

            except IntegrityError:
                return render(request,"pages/signupuser.html", {"form": UserCreationForm, "error":"That userame has taken"})

        else:
            return render(request,"pages/signupuser.html", {"form": UserCreationForm, "error":"Passwords did not match"})

def loginuser(request):
    if request.method == "GET":
        return render(request,"pages/loginuser.html", {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"]) # doğrulama yapamadıysa None değer döner
        if user == None:
            return render(request,"pages/loginuser.html", {"form":AuthenticationForm(), "error":"Username and Password did not match!"})
        else:
            login(request, user)
            return redirect("/")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")