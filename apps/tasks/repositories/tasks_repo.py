from rest_framework.generics import get_object_or_404

from apps.tasks.models import Task


class TasksRepository:
    def get_all_tasks(self):
        return Task.objects.all()

    def get_task_by_pk(self, pk):
        return get_object_or_404(Task, id=pk)

    def create_task(self, data):
        task = Task.objects.create(**data)

        return task
