from django.urls import path
from .views import TaskCreateAPIView, TaskAssignmentAPIView, UserTasksAPIView

urlpatterns = [
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/assign/', TaskAssignmentAPIView.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', UserTasksAPIView.as_view(), name='user-tasks'),
]
