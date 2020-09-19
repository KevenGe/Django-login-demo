from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


class Question(models.Model):
    question_text = models.CharField(max_length=40)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=40)
    votes = models.IntegerField()
