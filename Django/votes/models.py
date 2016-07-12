from django.db import models

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choise(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    choise_date = models.DateTimeField('date choise')
    choise_date = models.DateTimeField('date choise')