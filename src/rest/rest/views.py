from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .services import TodoService

class TodoListView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = TodoService()

    def get(self, request):
        todos = self.service.get_all_todos()
        return Response(todos, status=status.HTTP_200_OK)
        
    def post(self, request):
        data = request.data
        if not data:
             return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        todo_id = self.service.create_todo(data)
        return Response({"id": todo_id, "message": "Todo created successfully"}, status=status.HTTP_201_CREATED)

