from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo

# Create your views here.
class TodoListCreate(generics.ListCreateAPIView): 
  # ListAPIView is a built-in generic class which creates a
  # read-only endpoint for model instances.
  # ListAPIView requires two mandatory attributes, serializer_class and queryset.
  # We specify TodoSerializer which we have earlier implemented serializer_class = TodoSerializer
  serializer_class = TodoSerializer
  permission_classes = [permissions.IsAuthenticated]
  # With permissions, we can grant or deny access for different classes of users to different parts of the API.
  
  def get_queryset(self):
    user = self.request.user
    
    return Todo.objects.filter(user=user).order_by('-created')
  
  def perform_created(self, serializer):
    # serializer holds a django model
    user = self.request.user
    print('user =', user)
    serializer.save(user=user) 
    # perform_create acts as a hook which is called before the instance is created in the database. Thus, we can specify
    # that we set the user of the todo as the request’s user before creation in the database.
    # These hooks are particularly useful for setting attributes that are implicit in the request, but are not part of the
    # request data. In our case, we set the todo’s user based on the request user.
  
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
