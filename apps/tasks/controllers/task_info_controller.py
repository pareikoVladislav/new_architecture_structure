from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.tasks.services.tasks_services import TasksService


class TaskInfoController(APIView):
    service = TasksService()

    def get(self, request: Request, *args, **kwargs):
        task_id = kwargs.get("task_id")

        if task_id:
            task_info = self.service.get_task_info_by_task_id(
                task_id=task_id
            )

            return Response(
                status=status.HTTP_200_OK,
                data=task_info
            )
