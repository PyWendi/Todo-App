from django.db import models

# Create your models here.

"""USER TABLE"""
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=False)
    tel = models.CharField(max_length=15)
    pwd = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.lname

"""TASKS TABLE"""
class Task(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    description = models.TextField()
    date = models.DateField("date_published")
    time = models.TimeField("time_published")

    def __str__(self):
        return self.title