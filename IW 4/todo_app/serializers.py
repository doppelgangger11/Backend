from rest_framework import serializers

from .models import Todo, TodoList


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, min_length=10, allow_null=False, allow_blank=False)

    def create(self, validated_data):
        todo_list = TodoList(**validated_data)
        todo_list.save()
        return todo_list
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance
    

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, min_length=10, allow_null=False, allow_blank=False)
    todo_list = TodoListSerializer(allow_null=False, read_only=True)
    todo_list_id = serializers.IntegerField(write_only=True)
    def create(self, validated_data):
        todo = Todo(**validated_data)
        todo.save()
        return todo
    

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name')
        instance.todo_list = validate_data.get('todo_list')
        instance.save()
        return instance
    