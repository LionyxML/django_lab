from rest_framework import viewsets
from .serializers import TodoSerializer

from .models import Todo


class TodoListView(viewsets.ModelViewSet):
    model = Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
