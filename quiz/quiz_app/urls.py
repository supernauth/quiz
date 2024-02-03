from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question", views.add_question),
    path("question/addrecord", views.add_question_record),
    path("question/uptate/<ind:id>", views.update_question),
    path("question/update/updaterecord/<ind:id>", views.update_question_record),
    path("question/delete=<ind:id>", views.delete_question),
]
