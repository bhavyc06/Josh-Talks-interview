from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    # Allow assigning tasks by providing user IDs.
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'created_at',
            'task_type', 'completed_at', 'status', 'assigned_to'
        ]
        read_only_fields = ['created_at']
