from django.urls import path

from apps.tasks.controllers.all_tasks_controller import (
    AllTasksController,
)
from apps.tasks.controllers.task_info_controller import (
    TaskInfoController,
)


urlpatterns = [
    path("", AllTasksController.as_view()),
    path("<int:task_id>/", TaskInfoController.as_view()),
]
