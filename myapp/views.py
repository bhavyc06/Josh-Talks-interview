from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer

# API to create a task.
class CreateTaskAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API to assign a task to one or multiple users.
class AssignTaskAPIView(APIView):
    def post(self, request, task_id):
        # Retrieve the task object or return 404 if not found.
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Expect a JSON body with "user_ids": [list_of_ids]
        user_ids = request.data.get('user_ids', [])
        if not isinstance(user_ids, list):
            return Response({"error": "user_ids must be a list"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve users that exist with given IDs.
        users = User.objects.filter(id__in=user_ids)
        if not users.exists():
            return Response({"error": "No valid users found for the given IDs"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Assign the retrieved users to the task.
        task.assigned_to.add(*users)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API to get tasks for a specific user.
class UserTasksAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        # Return tasks assigned to the user with given ID.
        return Task.objects.filter(assigned_to__id=user_id)
