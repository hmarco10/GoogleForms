from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/', views.QuestionList.as_view())
    
]

#urlpatterns = [
#    path('', views.AnswerList.as_view()),
#]
