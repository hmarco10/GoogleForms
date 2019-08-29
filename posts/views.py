from django.shortcuts import render

from rest_framework import generics, viewsets

from .models import Post, Answer, Questions
from .serializers import PostSerializer, AnswerSerializer, QuestionsSerializer

from django.db.models import Count
# Create your views here.


#Vistas para crear
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    Answer.objects.filter(answer='20')
    serializer_class = AnswerSerializer

#vistas para detalle actualizar y eliminar
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Questions.objects.all()
    serializer_class = QuestionsSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

