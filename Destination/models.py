# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20) #用户名称，字符型，最大长度20
    age = models.IntegerField() #用户年龄，整型

class Question(models.Model):
    question_text = models.CharField(max_length=200)#题目名称，字符型，最大长度200
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
