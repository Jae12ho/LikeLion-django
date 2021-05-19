from django.db import models

# Create your models here.

class Store(models.Model):
    title = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    detail = models.TextField()
    enpl_area = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)
    todo = models.CharField(max_length=200)
    appl_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def cnt(self):
        self.appl_num += 1
        self.save()
        return self.appl_num

    def dcnt(self):
        self.appl_num -= 1
        self.save()
        return self.appl_num