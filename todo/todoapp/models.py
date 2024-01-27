from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=300, null=False)
    created_by = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Priority(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    created_by = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    created_by = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=300, null=False)
    status = models.CharField(max_length=30, null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks_category')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='tasks_priority')

    def __str__(self):
        return self.title
