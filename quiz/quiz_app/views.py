from django.shortcuts import render
from quiz_app.models import Question, User, UserAnswer


def index(request):
    questions = Question.objects.all()
    return render(request, "index.html", {"questions": questions})
