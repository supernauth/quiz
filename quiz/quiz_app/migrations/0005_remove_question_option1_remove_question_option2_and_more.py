# Generated by Django 5.0 on 2024-02-04 20:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quiz_app", "0004_alter_question_correct_option_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="option1",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option2",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option3",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option4",
        ),
    ]
