from django.shortcuts import render
from .models import Question
from .models import Answer

def index(request):
    all_questions = Question.objects.all()
    all_answers = Answer.objects.all()
    context = {
        'all_questions': all_questions,
        'all_answers' : all_answers,
    }
    return render(request, 'demo/index.html', context)
