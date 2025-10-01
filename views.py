from rest_framework import viewsets
from rest_framework.response import Response

class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        tasks = [
            {"id": 1, "name": "Letter to a Character"},
            {"id": 2, "name": "Paint an Old T-shirt"},
            {"id": 3, "name": "Bottle Art"},
            {"id": 4, "name": "Mud Sculpting"}
        ]
        return Response(tasks)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard_data = [
            {"user": "Alice", "points": 50},
            {"user": "Bob", "points": 40},
            {"user": "You", "points": 0}  # Placeholder for your rank
        ]
        return Response(leaderboard_data)

class SubmissionViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        return Response({"message": "Task submitted successfully", "data": data})
