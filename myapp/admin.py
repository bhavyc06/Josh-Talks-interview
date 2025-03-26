from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Task

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Extend the default UserAdmin to display the mobile field.
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)}),
    )
    list_display = ('id', 'username', 'name', 'email', 'mobile')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_at')
    list_filter = ('status', 'task_type')
