from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from todo.models import Todo

# Create your views here.
class TodoListCreate(generics.ListCreateAPIView): 
  # ListAPIView is a built-in generic class which creates a
  # read-only endpoint for model instances.
  # ListAPIView requires two mandatory attributes, serializer_class and queryset.
  # We specify TodoSerializer which we have earlier implemented serializer_class = TodoSerializer
  serializer_class = TodoSerializer
  
  def get_queryset(self):
    user = self.request.user
    
    return Todo.objects.filter(user=user).order_by('-created')
  
    """
    Code explanation
    We import DRF ’ s generics class of views.
    We then create TodoList that uses generics.ListAPIView. ListAPIView is a built-in generic class which creates a
    read-only endpoint for model instances. ListAPIView requires two mandatory attributes which are serializer_class
    and queryset.
    When we specify TodoSerializer as the serializer class, we create a read-only endpoint for todo instances. There are
    many other generic views available and we explore them later.
    get_queryset returns the queryset of todo objects for the view. In our case, we specify the query set as all todos
    which match the user. Additionally, we order the todos by the created date i.e. we show the latest todo first. You
    can customize get_queryset to return the set of todos that you want.
    """
