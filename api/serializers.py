from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
  created = serializers.ReadOnlyField()
  completed = serializers.ReadOnlyField()
  
  class Meta:
    model = Todo
    fields = ['user', 'title', 'memo', 'created', 'completed']
    
  """
  Code Explanation
  class TodoSerializer(serializers.ModelSerializer):
    We extend DRF’s ModelSerializer into a TodoSerializer class. ModelSerializer provides an API to create serializers
    from your models.
    
    class Meta:
      model = Todo
      fields = ['id','title','memo','created','completed']
  Under class Meta, we specify our database model Todo and the fields we want to expose i.e.
  ['id','title','memo','created','completed']. Django REST Framework then magically transforms our model data into
  JSON, exposing these fields from our Todo model.
  Fields not specified here will not be exposed in the API. Remember that ‘id’ is created automatically by Django so
  we didn’t have to define it in Todo model. But we will use it in our API.
  Often, an underlying database model will have more fields than what needs to be exposed. DRF’s serializer class’s
  ability to include/exclude fields in our API is a great feature and makes it straightforward to control this.
  Additionally, we specify that created and completed fields are read only. I.e., they cannot be edited by a user
  (because they ought to be auto-populated when a todo is created and when it is marked as complete).
  """  
  
class TodoToggleCompleteSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Todo
    fields = ['user'] # why need to show id?
    read_only_fields = ['title', 'memo', 'completed', 'created']
    