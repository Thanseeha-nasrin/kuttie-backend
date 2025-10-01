from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submission_file = models.CharField(max_length=255, default='default.png')  # You can use FileField later if storing files
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task.name}"

# Optional: Leaderboard can be calculated dynamically from Submissions
