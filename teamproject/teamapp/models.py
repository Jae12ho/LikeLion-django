from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    school_num = models.TextField()
    birth = models.DateField()
    favor_food = models.CharField(max_length=200, default='d', blank=True)
    birth_loca = models.CharField(max_length=200)
    intro = models.TextField()
    mbti = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
    