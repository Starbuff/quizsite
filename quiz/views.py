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

def quiz_qa_tp(request):
	return render(request, "quiz/quiz_qa_tp.html")

def quiz_results_tp(request):
	return render(request, "quiz/quiz_results_tp.html")