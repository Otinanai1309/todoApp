from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo

from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate


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
    
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TodoSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    # user can only update, delete own posts
    
    return Todo.objects.filter(user=user)
  
class TodoToggleComplete(generics.UpdateAPIView):
  serializer_class = TodoToggleCompleteSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  
  def get_queryset(self):
    user = self.request.user
    """todoObject = Todo.objects.filter(user=user)
    todoObject.title = self.title
    todoObject.memo = self.memo"""
    
    return Todo.objects.filter(user=user)
  
  def perform_update(self, serializer):
    
    serializer.instance.completed = not(serializer.instance.completed)
    return serializer.save()
  
  
@csrf_exempt
def signup(request):
  if request.method == 'POST':
    try:
      data = JSONParser().parse(request)  # data is a dictionary
      user = User.objects.create_user(
        username = data['username'],
        password=data['password']
      )
      user.save()
      
      token = Token.objects.create(user=user)
      return JsonResponse({'token':str(token)}, status=201)
    except IntegrityError:
      return JsonResponse({'error':'username taken, choose another username'}, status=400)


@csrf_exempt
def login(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    user = authenticate(
      request,
      username=data['username'],
      password=data['password']
    )
    if user is None:
      return JsonResponse({'error':'unable to login. Check username or password'}, status=400)
    else:  #return user token
      try:
        token = Token.objects.get(user=user)
      except:  # if token not in db, create a new one
        token = Token.objects.create(user=user)
      return JsonResponse({'token':str(token)}, status=201)