from django.shortcuts import render

# Create your views here.
from rest_framework import generics
#
# from todos import models
# from . import serializers
#
# class ListTodo(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer
#
# class UpdateTodo(generics.UpdateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer
#     # pagination_class =
#
# class DestroyTodo(generics.DestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer


# Most API endpoints are some combination of common CRUD (Create-Read-Update-Delete) functionality.
# Instead of writing these views one-by-one in our views.py file as well as providing individual
# routes for each in our urls.py file we can instead use a ViewSet which abstracts away much of this work.

# api/views.py
from rest_framework import viewsets

from todos import models
from . import serializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer