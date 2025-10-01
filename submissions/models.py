from django.db import models

class Submission(models.Model):
    task_id = models.IntegerField()
    user = models.CharField(max_length=100)
    submission = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - Task {self.task_id}"
