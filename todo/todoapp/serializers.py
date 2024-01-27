from datetime import datetime

from rest_framework import serializers

from .models import Task, Category, Priority


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'completed_at', 'updated_at', 'deleted_at', 'deleted']

    def create(self, validated_data):
        return Task.objects.create(
            id=validated_data['id'],
            created_by=self.context['user'],
            title=validated_data['title'],
            description=validated_data['description'],
            status=validated_data['status'],
            completed=validated_data['completed'],
            created_at=datetime.now(),
            category=validated_data['category'],
            priority=validated_data['priority']

        )

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.status = validated_data.get("status", instance.status)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.completed_at = datetime.now()
        instance.updated_at = datetime.now()
        instance.category = validated_data.get("category", instance.category)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'deleted_at', 'deleted']

    def create(self, validated_data):
        return Category.objects.create(
            id=validated_data['id'],
            created_by=self.context['user'],
            name=validated_data['name'],
            description=validated_data['description'],
            created_at=datetime.now(),

        )

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.updated_at = datetime.now()
        instance.save()
        return instance

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'deleted_at', 'deleted']

    def create(self, validated_data):
        return Priority.objects.create(
            id=validated_data['id'],
            created_by=self.context['user'],
            name=validated_data['name'],
            created_at=datetime.now(),

        )

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.updated_at = datetime.now()
        instance.save()
        return instance