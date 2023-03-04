from django.db import models


class TodoList(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'

class Todo(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    todo_list = models.ForeignKey(TodoList, null=False, on_delete=models.RESTRICT)
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'