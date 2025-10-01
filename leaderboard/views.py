from rest_framework import viewsets, serializers
from rest_framework.response import Response
from submissions.models import Submission
from django.db.models import Count

# Simple leaderboard serializer
class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField()
    total_submissions = serializers.IntegerField()

# Example ViewSet for leaderboard
class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        # Aggregate submissions per user
        data = Submission.objects.values('user').annotate(total_submissions=Count('id')).order_by('-total_submissions')
        return Response(data)
