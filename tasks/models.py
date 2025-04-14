from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extended user model with additional fields"""
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email


class Task(models.Model):
    """Task model representing various tasks in the system"""
    TASK_TYPE_CHOICES = (
        ('PERSONAL', 'Personal'),
        ('WORK', 'Work'),
        ('URGENT', 'Urgent'),
        ('OTHER', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default='OTHER')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_users = models.ManyToManyField(User, related_name='assigned_tasks')

    def __str__(self):
        return self.name
