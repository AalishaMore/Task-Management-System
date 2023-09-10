from django.shortcuts import render
from rest_framework.response import Response
from .models import Project, Tasks
from .serializers import ProjectSerializer, TasksSerializer
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET'])
def ApiOverview(request):
    if request.method == 'GET':
        api_urls = {
            # project urls(endpoint)
            'Add/Create': '/projects/',                                   # List all project[GET/POST]                 
            'View/Update/Delete Project': '/projects/<int:pk>/',           # View/Update/Delete [GET/PUT/DELETE]
        
            # task urls(endpoints)
            'All Tasks': '/tasks/',                                 # List all tasks
            'View/Update/Delete Task':  '/tasks/<int:pk>/',         # [View/Update/Delete [GET/PUT/DELETE]
        }
    return Response(api_urls)



@api_view(['GET', 'POST'])
def project_list_create(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET': 
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    

@api_view(['GET','PUT','DELETE'])
def project_detail(request, pk):
    # project = None
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tasks = Tasks.objects.filter(project=project)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
        
    
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def task_list_create(request):
    if request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            project_id = request.data.get('project')
            try:
                project = Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                return Response({'project' : ['Invalid project ID - object does not exists']}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        task = Tasks.objects.all()
        serializer = TasksSerializer(task, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task = Tasks.objects.get(pk=pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
