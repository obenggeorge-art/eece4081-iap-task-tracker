
from django.db import models


class Task(models.Model):
    TASK_TYPES = [
        ("Assignment", "Assignment"),
        ("Exam", "Exam"),
        ("Project", "Project"),
        ("Other", "Other"),
    ]

    PRIORITIES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TASK_TYPES)
    dueDate = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
