from rest_framework import viewsets, serializers
from .models import Submission

# Serializer for Submission model
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'  # task_id, user, submission, timestamp

# ViewSet for Submission API
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
