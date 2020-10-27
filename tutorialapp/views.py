from django.shortcuts import render
from rest_framework import generics
from .models import Tutorial
from .serializers import TutorialSerializer

# Create your views here.

class ListTutorialView(generics.ListAPIView):
    '''
    Provides a get method handler.
    '''
    
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
