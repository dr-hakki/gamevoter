from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Question, Choice, Application, New
from django import forms
from django.contrib import messages
from django.forms import ModelForm
from django.forms import inlineformset_factory,formset_factory



class NameForm(forms.Form):
    searched = forms.CharField(max_length=100)

# Get questions and display them
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def indexaction(request):
    latest_question_list = Question.objects.filter(category="action")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Action Polls"}
    return render(request, 'polls/index.html', context)
def indexfps(request):
    latest_question_list = Question.objects.filter(category="fps")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"FPS Polls"}
    return render(request, 'polls/index.html', context)
def indexmoba(request):
    latest_question_list = Question.objects.filter(category="moba")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"MOBA Polls"}
    return render(request, 'polls/index.html', context)
def indexracing(request):
    latest_question_list = Question.objects.filter(category="racing")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Racing Polls"}
    return render(request, 'polls/index.html', context)
def indexrpg(request):
    latest_question_list = Question.objects.filter(category="rpg")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"RPG Polls"}
    return render(request, 'polls/index.html', context)
def indexstrategy(request):
    latest_question_list = Question.objects.filter(category="strategy")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Strategy Polls"}
    return render(request, 'polls/index.html', context)
def indexsports(request):
    latest_question_list = Question.objects.filter(category="sports")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Sports Polls"}
    return render(request, 'polls/index.html', context)
def indexsimulation(request):
    latest_question_list = Question.objects.filter(category="simulation")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Simulation Polls"}
    return render(request, 'polls/index.html', context)
def indexstory(request):
    latest_question_list = Question.objects.filter(category="story")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Games With Stories Polls"}
    return render(request, 'polls/index.html', context)
def indexotherg(request):
    latest_question_list = Question.objects.filter(category="otherg")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Other Polls"}
    return render(request, 'polls/index.html', context)
def indexseries(request):
    latest_question_list = Question.objects.filter(xcategory="series")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Best Game of the Series"}
    return render(request, 'polls/index.html', context)
def indexcomparison(request):
    latest_question_list = Question.objects.filter(xcategory="comparison")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Game Comparison Polls"}
    return render(request, 'polls/index.html', context)
def indexplayer(request):
    latest_question_list = Question.objects.filter(xcategory="player")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Best e-Sports Players"}
    return render(request, 'polls/index.html', context)
def indexteam(request):
    latest_question_list = Question.objects.filter(xcategory="team")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Best e-Sports Teams"}
    return render(request, 'polls/index.html', context)
def indexother(request):
    latest_question_list = Question.objects.filter(xcategory="other")[::-1]
    context = {'latest_question_list': latest_question_list,"baslik":"Others"}
    return render(request, 'polls/index.html', context)
def indexpopular(request):
    latest_question_list = Question.objects.filter(popular=True)[::-1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/indexpopular.html', context)


def profile(request):
    qlist = Question.objects.filter(creator=request.user.username)
    user = request.user
    if user.has_perm('polls.add_question'):
        left = Application.objects.get(username=request.user.username)
        context = {'qlist': qlist,"username":request.user.username,"email":left.email,"left":left.left}
    else:
        context = {"username":request.user.username}
    return render(request, 'pages/profile.html', context)

def faq(request):
    support = Application.objects.get(username="support")
    return render(request, 'pages/faq.html',{"support":support})


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
  elif question.choice_number == 6:
      return render(request, 'polls/results6.html', { 'question': question })
  elif question.choice_number == 7:
      return render(request, 'polls/results7.html', { 'question': question })

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

class ApplicationForm(forms.Form):
    username = forms.CharField(max_length=100,disabled=True)
    email = forms.EmailField(required=True,widget=forms.Textarea)
    cv = forms.CharField(required=True,max_length=250,label="Please write the name of your professional accounts (Steam, EpicGames, RiotGames etc. ")
    gameids = forms.CharField(required=True,max_length=150)

def application(request):
    if request.method == "GET":
        return render(request,"pages/application.html", {"form": ApplicationForm})
    else:
        try:
            application = Application(username= request.user.username,email=request.POST["email"],cv= request.POST["cv"],gameids=request.POST["gameids"])
            application.save()
            messages.success(request,  'Your application has been received successfully. Extra applications reduce your chances of acceptance.')
            return redirect("/")

        except IntegrityError:
            return render(request,"pages/application.html", {"form": ApplicationForm, "error":"Enter all the information please!"})


def news(request):
    news = New.objects.order_by('-pub_date')[:40]
    return render(request, 'pages/news.html', { "news":news })

def newdetail(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'pages/newdetail.html', { "new":new })



class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["question_text","image","choice_number","category","xcategory","creator"]

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text","image"]



def createpoll(request):
    x = Application.objects.get(username=request.user.username)
    if x.left != 0 :
        ChoiceFormSet = formset_factory(ChoiceForm, extra=5,
                                        min_num=2, validate_min=True)
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        if request.method == 'POST':
            try:
                form = QuestionForm(request.POST,request.FILES)
                formset = ChoiceFormSet(request.POST, request.FILES)
                if all([form.is_valid(), formset.is_valid()]):
                    poll = form.save()
                    poll.creator = request.user.username
                    poll.save()
                    for inline_form in formset:
                        if inline_form.cleaned_data:
                            choice = inline_form.save(commit=False)
                            choice.question = poll
                            choice.save()
                    
                    x.left -= 1
                    x.save()
                    messages.success(request,  'Your poll has been created successfully.')
                    
                    return redirect("/")

                else:
                    return render(request,"pages/createpoll.html", {'form': form,'formset': formset,"error":"Enter all the information please!"})

            except:
                return render(request,"pages/createpoll.html", {'form': form,'formset': formset,"error":"Enter all the information please!"})

        else:
            form = QuestionForm()
            formset = ChoiceFormSet()

        return render(request, 'pages/createpoll.html', {'form': form,
                                                    'formset': formset})

    else:
        messages.warning(request,  'You ran out of right to create polls!')
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        return render(request, 'pages/index.html',{"form": NameForm,"latest_question_list":latest_question_list})



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