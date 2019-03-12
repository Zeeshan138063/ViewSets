from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.permissions import IsOwnerOrReadOnly
from .serializers import *

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
from .pagination import (
PostPageNumberPagination
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# a single entry point to our API

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users-list': reverse('user-list', request=request, format=format),
        # 'users': reverse('user', request=request, format=format),
        # 'snippets': reverse('snippet', request=request, format=format),
        'snippets-list': reverse('snippest-list', request=request, format=format)

    })

# First, we're using REST framework's reverse function in order to return fully-qualified URLs;
# second, URL patterns are identified by convenience names
# that we will declare later on in our snippets/urls.py.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    pagination_class = PostPageNumberPagination

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework import generics
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)