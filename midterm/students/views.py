import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from students.models import students
from students.serializers import studentsSerializer


@csrf_exempt
def students_handler(request):
    if request.method == 'GET':
        categories = students.objects.all()
        serializer = studentsSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = studentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_students(pk):
    try:
        students = students.objects.get(id=pk)
        return {
            'status': 200,
            'students': students
        }
    except students.DoesNotExist as e:
        return {
            'status': 404,
            'students': None
        }


@csrf_exempt
def students_handler(request, pk):
    result = get_students(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'students not found'}, status=404)

    students = result['students']

    if request.method == 'GET':
        serializer = studentsSerializer(students)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = studentsSerializer(data=data, instance=students)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        students.delete()
        return JsonResponse({'message': 'students deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)


