from django.shortcuts import render

# coding: utf-8
def quiz_main(request):
	return render(request, "quiz/quiz_main.html"),
def quiz_start_tp(request):
	return render(request, "quiz/quiz_start_tp.html"),
def quiz_qa_tp(request):
	return render(request, "quiz/quiz_qa_tp.html"),
def quiz_results_tp(request):
	return render(request, "quiz/quiz_results_tp.html"),