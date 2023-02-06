from django.urls import path
from . import views


urlpatterns = [
  path('todos/', views.TodoListCreate.as_view()),  
  path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
  path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
  path('signup/', views.signup),
]

"""
We have one route ‘/todos’ as a demonstration. What we want to achieve is that when a request is made to
localhost:8000/api/todos, you should get a JSON response with the list of todo instances. But how do we achieve
this?
The answer is in views.TodoList.as_view().
In traditional full stack Django projects, views are used to customize what data to send to the HTML templates. In
our API project, we use class-based generic views (from DRF) to similarly send customized serialized data but this
time, to the API endpoints instead of to templates.
views.TodoList is an instance of a class-based generic view. Django’s generic views help us quickly write views
(without having to write too much repetitive code) to do common tasks like:
- Display a list of objects, e.g. list of todos.
- Display detail pages for a single object. E.g. detail page of a todo.
- Allow users to create, update, and delete objects – with or without authorization.
"""