from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import TodoItem
from .serializers import TodoItemSerializer


# List all todos or create a new one
class TodoListCreate(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


# Retrieve, update, or delete a todo by id
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def get_object(self):
        try:
            return super().get_object()
        except TodoItem.DoesNotExist:
            raise NotFound(detail="Todo item not found", code=404)
