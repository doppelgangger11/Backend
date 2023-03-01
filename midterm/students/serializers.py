from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=75, allow_null=False)
    description = serializers.CharField(allow_null=False, allow_blank=True, default='')

    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance