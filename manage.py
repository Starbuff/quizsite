#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizsite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

class Quiz(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, related_name="questions")
	question = models.TextField()
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()
