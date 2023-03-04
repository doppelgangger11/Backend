import json

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from todo_app.models import Todo, TodoList
from todo_app.serializers import TodoListSerializer, TodoSerializer


@csrf_exempt
def todo_lists_handler(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        serializer = TodoListSerializer(todo_lists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message':'Request is not supported'}, safe = False)

def get_todo_list(pk):
    result = {'todo_list': None}
    try:
        result['todo_list'] = TodoList.objects.get(id=pk)
    except TodoList.DoesNotExist:
        result['todo_list'] = None
    

    return result

def get_todo(pk):
    result = {'todo': None}
    try:
        result['todo'] = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        result['todo'] = None

    return result    





@csrf_exempt
# todo_list 
def todo_lists_handler(request, pk):
    result = get_todo_list(pk)
    if result['todo_list'] is None:

    
        return JsonResponse({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)
        
    todo_list = result['todo_list']

    if request.method == 'GET':
        serializer = TodoListSerializer(todo_list, many=False)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        # return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'PUT':
            data = json.loads(request.body)
            serializer = TodoListSerializer(data=data, instance=todo_list)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    elif request.method == 'DELETE':
        todo_list.delete()
        return JsonResponse({'message': "Todo List is deleted successfully!"}, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)

@csrf_exempt
def todo_list_handler(request, pk):
    result = get_todo_list(pk)
    if result['todo_list'] is None:
        return JsonResponse({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)
        
    todo_list = result['todo_list']


    if request.method == 'GET':
        todos = todo_list.todo_set.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = json.loads(result.body)
        data['todo_list_id'] = pk
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)




@csrf_exempt
def todo_handler(request, pk):
    result = get_todo(pk)
    todo = result['todo']
    
    if result['todo_list'] is None:
        return JsonResponse({'message': 'Tod List not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        data['todo_list_id'] = pk
        serializer = TodoSerializer(data=data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)