from django.urls import path
from .views import CreateTaskAPIView, AssignTaskAPIView, UserTasksAPIView

urlpatterns = [
    path('tasks/create/', CreateTaskAPIView.as_view(), name='create-task'),
    path('tasks/<int:task_id>/assign/', AssignTaskAPIView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksAPIView.as_view(), name='user-tasks'),
]
