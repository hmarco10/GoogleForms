from rest_framework import serializers
from .import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('User','GoogleForm','description','created_at','updated_at',)
        
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ('GoogleForm','question','created_at','updated_at',)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('question','answer','created_at',)
       

