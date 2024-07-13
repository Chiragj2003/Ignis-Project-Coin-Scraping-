from rest_framework import serializers
from .models import Job, Task

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_id', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['coin', 'output']