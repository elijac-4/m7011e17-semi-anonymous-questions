from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=128)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)

    def __str__(self):
        return self.answer_text
