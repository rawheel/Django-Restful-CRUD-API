from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class EventList(generics.ListCreateAPIView): # for just GET request
    queryset = Event.objects.all()
    serializer_class = EventSerializer
class EventDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

