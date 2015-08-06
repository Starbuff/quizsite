from django.shortcuts import render
# coding: utf-8

quizzes = {
	"Twin_Peaks": {
   		"name": u"Twin Peaks",
	   	"description": u"Hur väl kommer du ihåg TV-serien?"
	},
	"Battlestar_Galactica": {
	   	"name": u"Battlestar Galactica",
	   	"description": u"Hur väl kommer du ihåg TV-serien?"
	},
	"House_M.D.": {
	    	"name": u"House M.D.",
	    	"description": u"Hur väl kommer du ihåg TV-serien?"	},
}


def quiz_main(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/quiz_main.html", context)

def quiz_start_tp(request):
	return render(request, "quiz/quiz_start_tp.html")

def quiz_qa_tp(request, slug, number):
	context = {
	"question_number": number,
   	"question": u"Hur många bultar har ölandsbron?",
	"answer1": u"12",
  	"answer2": u"66 400",
   	"answer3": u"7 428 954",
   	"quiz_slug": slug,
}
	return render(request, "quiz/quiz_qa_tp.html")

def quiz_results_tp(request, slug):
	context = {
	   	"correct": 12,
	   	"total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz_results_tp.html", context)
