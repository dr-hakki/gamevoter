from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings

class Question(models.Model):
    popular = models.BooleanField(null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    image = models.ImageField(upload_to="polls/images/",blank=True)
    choice_number = models.IntegerField(default=2,help_text="Maximum is 7")
    category = models.CharField(max_length=50, default="action", help_text="All lowercase")
    xcategory = models.CharField(max_length=50, default="game comparison")
    vdq = models.ManyToManyField(User,blank=True, related_name="user_voted")
    creator = models.CharField(max_length=50, help_text="If you leave this blank, your username will not be published, only admins can see it.")
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    image = models.ImageField(upload_to="polls/images/",blank=True)
    votes = models.IntegerField(default=0,editable=True) # KULLANICILARA POLL İZNİ VERİNCE EDİTABLE I KAPAT

    def __str__(self):
        return self.choice_text

class Application(models.Model):
    checked = models.BooleanField(null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    cv = models.CharField(max_length=250,help_text="Write about your gaming history!")
    gameids = models.CharField(max_length=150, help_text="Please write the name of your professional accounts (Steam, EpicGames, RiotGames etc. ")
    left = models.IntegerField(default=10)
    def __str__(self):
        return self.username

class New(models.Model):
    head= models.CharField(max_length=150)
    image = models.ImageField(upload_to="polls/images/",blank=True)
    image2 = models.ImageField(upload_to="polls/images/",blank=True)
    image2text = models.CharField(max_length=500,blank=True)
    image3 = models.ImageField(upload_to="polls/images/",blank=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.head