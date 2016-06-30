from django.db import models

class Question(models.Model):
    quesrion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    choise_date = models.DateTimeField('date choise')