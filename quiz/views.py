# coding: utf-8
from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

# quizzes = {
# 	"klassiker": {
#  	   	"name": u"Twin Peaks",
# 	    	"description": u"Hur väl kommer du ihåg TV-serien?"
# 	 },
# 	 "fotboll": {
#   	   	"name": u"Battlestar Galactica",
#   	   	"description": u"Hur väl kommer du ihåg TV-serien?"
#   	},
#   	"kanda-hackare": {
#   	    	"name": u"House M.D.",
#   	    	"description": u"Hur väl kommer du ihåg TV-serien?"	}, 
# }

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	number = int(number)
	quiz = Quiz.objects,get(slug=slug)
	questions = quiz.questions.all()
	question = question[number - 1]
	if number > questions.count():
		return redirect("completed:page", quiz.slug)

	context = {
	"question_number": number,
   	"question": question.question,
	"answer1": question.answer1,
  	"answer2": question.answer2,
   	"answer3": question.answer3,
   	"quiz": quiz,
}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	   	"correct": 12,
	   	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)
