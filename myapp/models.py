from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model extending AbstractUser.
class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)

    @property
    def name(self):
        # Return full name or username if first/last not provided.
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username

    def __str__(self):
        return self.name

# Task model representing a task in the system.
class Task(models.Model):
    # Define choices for task status and type.
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    TASK_TYPE_CHOICES = [
        ('feature', 'Feature'),
        ('bug', 'Bug'),
        ('improvement', 'Improvement'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default='feature')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='pending')
    # Many-to-many: a task can be assigned to multiple users.
    assigned_to = models.ManyToManyField(User, related_name='tasks', blank=True)

    def __str__(self):
        return self.name
