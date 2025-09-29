from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# GET /tasks
@api_view(['GET'])
def tasks_list(request):
    tasks = [
        {"id": 1, "name": "Task 1"},
        {"id": 2, "name": "Task 2"}
    ]
    return Response(tasks)

# GET /leaderboard
@api_view(['GET'])
def leaderboard(request):
    leaderboard_data = [
        {"user": "Alice", "points": 50},
        {"user": "Bob", "points": 40}
    ]
    return Response(leaderboard_data)

# POST /submit
@api_view(['POST'])
def submit_task(request):
    data = request.data  # JSON data sent from client
    return Response({"message": "Task submitted successfully", "data": data})
