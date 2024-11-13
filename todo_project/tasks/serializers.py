# tasks/serializers.py

from rest_framework import serializers
from .models import User, Task  # Import your models here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'date_joined', 'is_active']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Replace with your Task model name
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']  # Replace with actual Task fields
