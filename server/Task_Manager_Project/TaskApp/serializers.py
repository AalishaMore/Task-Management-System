from rest_framework import serializers
from .models import Project, Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class ProjectSerializer(serializers. ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    
    def get_tasks(self, obj):
        tasks = Tasks.objects.filter(project=obj)
        task_serializer = TasksSerializer(tasks, many=True, source='tasks_set')
        return task_serializer.data
    
# class TasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tasks
#         fields = '__all__'