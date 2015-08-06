from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.startpage, name="startpage"),
	url(r"^quiz/([a-z-]+)/$", views.quiz, name="quiz"),
	url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name="question"),
	url(r"^quiz/([a-z-]+)/completed/$", views.completed, name="completed"),
	
]