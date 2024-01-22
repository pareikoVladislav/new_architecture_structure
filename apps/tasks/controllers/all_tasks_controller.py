from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.tasks.services.tasks_services import TasksService


class AllTasksController(APIView):
    service = TasksService()

    def get(self, request: Request, *args, **kwargs):
        tasks = self.service.get_all_tasks()

        return Response(
            status=status.HTTP_200_OK,
            data=tasks
        )

    def post(self, request: Request, *args, **kwargs):
        new_task = self.service.create_new_task(
            data=request.data
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=new_task
        )
