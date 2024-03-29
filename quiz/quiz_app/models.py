from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text


class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_option = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "question")

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"
