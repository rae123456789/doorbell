import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add = True)
    author_name = models.CharField(max_length=100, default='admin')
    voters = models.ManyToManyField(User, related_name='questions_voted_for')
 
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.PositiveSmallIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text