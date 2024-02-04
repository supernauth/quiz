from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from quiz_app.models import Question, User, UserAnswer


def index(request):
    questions = Question.objects.all()
    return render(request, "index.html", {"questions": questions})


def add_question(request):
    return HttpResponse(loader.get_template("question.html").render({}, request))


def add_question_record(request):
    Question(
        question_text=request.POST.get("question_text"),
        correct_option=request.POST.get("correct_option"),
    ).save()
    return HttpResponseRedirect(reverse("index"))


def update_question(request, id):
    return HttpResponse(
        loader.get_template("question.html").render(
            {"question": Question.objects.get(id=id)}, request
        )
    )


def update_question_record(request, id):
    question = Question.objects.get(id=id)
    question.question_text = request.POST.get("question_text")
    question.correct_option = request.POST.get("correct_option")
    question.save()
    return HttpResponseRedirect(reverse("index"))


def delete_question(request, id):
    Question.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("index"))
