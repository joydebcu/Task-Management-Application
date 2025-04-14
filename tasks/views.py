from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer, TaskAssignmentSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    """API endpoint to create a new task"""
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TaskAssignmentAPIView(generics.GenericAPIView):
    """API endpoint to assign a task to users"""
    serializer_class = TaskAssignmentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        task_id = serializer.validated_data['task_id']
        user_ids = serializer.validated_data['user_ids']
        
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {"error": f"Task with id {task_id} does not exist"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Get existing users and add them to the task
        users = User.objects.filter(id__in=user_ids)
        if len(users) != len(user_ids):
            found_ids = [user.id for user in users]
            missing_ids = [user_id for user_id in user_ids if user_id not in found_ids]
            return Response(
                {"error": f"Users with ids {missing_ids} do not exist"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Assign users to task
        task.assigned_users.add(*users)
        
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


class UserTasksAPIView(generics.ListAPIView):
    """API endpoint to get all tasks assigned to a specific user"""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Task.objects.filter(assigned_users__id=user_id)
