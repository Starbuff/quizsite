from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.quiz_main),
	url(r"^quiz/[a-z-]+/$", views.quiz_start_tp),
	url(r"^quiz/([a-z-]+/question/[0-9]+)/$", views.quiz_qa_tp),
	url(r"^quiz/[a-z-]+/completed/$", views.quiz_results_tp),
	
]