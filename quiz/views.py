from django.shortcuts import render
from quiz.models import Quiz
# coding: utf-8

#quizzes = {
	# "klassiker": {
 #   		"name": u"Twin Peaks",
	#    	"description": u"Hur väl kommer du ihåg TV-serien?"
	# },
	# "fotboll": {
 # 	   	"name": u"Battlestar Galactica",
 # 	   	"description": u"Hur väl kommer du ihåg TV-serien?"
 # 	},
 # 	"kanda-hackare": {
 # 	    	"name": u"House M.D.",
 # 	    	"description": u"Hur väl kommer du ihåg TV-serien?"	}, 
#}


def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
	"question_number": number,
   	"question": u"Hur många bultar har ölandsbron?",
	"answer1": u"12",
  	"answer2": u"66 400",
   	"answer3": u"7 428 954",
   	"quiz_slug": slug,
}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	   	"correct": 12,
	   	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)
