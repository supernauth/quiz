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
        option1=request.POST.get("option1"),
        option2=request.POST.get("option2"),
        option3=request.POST.get("option3"),
        option4=request.POST.get("option4"),
        answer=request.POST.get("answer"),
    ).save()
    return HttpResponseRedirect(reverse("index"))


def update_question(request, id):
    return HttpResponse(
        loader.get_template("question.html").render(
            {"question_text": Question.objects.get(id=id)}, request
        )
    )


def update_question_reqord(request, id):
    question = Question.objects.get(id=id)
    question.question_text = request.POST.get("quesiton_text")
    question.option1 = request.POST.get("option1")
    question.option2 = request.POST.get("option2")
    question.option3 = request.POST.get("option3")
    question.option4 = request.POST.get("option4")
    question.answer = request.POST.get("answer")
    question.save()
    return HttpResponseRedirect(reverse("index"))


def delete_question(request, id):
    Question.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("index"))
