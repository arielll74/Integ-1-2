from rest_framework import serializers
from .models import Post, Comment
#from django.contrib.auth import get_user_model

#User = get_user_model()

#class Serializer(serializers.ModelSerializer):
    #class Meta:
        #model = User
        #fields = ['email']

class PostSerializer(serializers.ModelSerializer):
    #author = Serializer
    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content']

#class CommentSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Comment
        #fields = '__all__'

