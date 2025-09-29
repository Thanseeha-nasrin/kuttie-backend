from django.db import models

class Submission(models.Model):
    TASK_CHOICES = [
        (1, "Letter to a Character"),
        (2, "Paint an old T-shirt"),
        (3, "Bottle art"),
        (4, "Mud Sculpting"),
    ]

    task_id = models.IntegerField(choices=TASK_CHOICES)
    user = models.CharField(max_length=50)
    submission = models.TextField(blank=True)  # text or image URL
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - Task {self.task_id}"
