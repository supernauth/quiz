from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question/add", views.add_question),
    path("question/add/addrecord", views.add_question_record),
    path("question/uptate/<int:id>", views.update_question),
    path("question/update/updaterecord/<int:id>", views.update_question_record),
    path("question/delete=<int:id>", views.delete_question),
]
