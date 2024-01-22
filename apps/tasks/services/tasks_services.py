from apps.tasks.repositories.tasks_repo import TasksRepository
from apps.tasks.serializers import AllTasksSerializer


class TasksService:
    tasks_repo = TasksRepository()
    serializer = AllTasksSerializer

    def get_all_tasks(self):
        tasks = self.tasks_repo.get_all_tasks()
        serializer = self.serializer(tasks, many=True)

        return serializer.data

    def get_task_info_by_task_id(self, task_id):
        task = self.tasks_repo.get_task_by_pk(
            pk=task_id
        )
        serializer = self.serializer(task)

        return serializer.data

    def create_new_task(self, data):
        serializer = self.serializer(
            data=data
        )

        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data

            new_task = self.tasks_repo.create_task(
                data=validated_data
            )

            return self.serializer(new_task).data

        else:
            return serializer.errors
