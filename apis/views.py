from django.shortcuts import render
from todos import models
from .serializers import TodoSerializer
from rest_framework import generics, permissions

# Create your views here.
class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class ListTodoRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    


