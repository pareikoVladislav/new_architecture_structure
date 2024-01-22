import datetime

from rest_framework import serializers

from apps.categories_statuses.models import (
    Category,
    Status,
)
from apps.tasks.error_messages import (
    TASK_TITLE_TOO_LONG_ERROR,
    WRONG_DEADLINE_ERROR,
    TASK_DESCRIPTION_TOO_LONG_ERROR,
)
from apps.tasks.models import Task


class TaskInfoSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'category',
            'status',
            'date_started',
            'deadline',
            'created_at',
            'subtasks'
        ]


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        title = data.get("title")
        description = data.get("description")
        deadline = data.get("deadline")

        if len(title) > 75:
            raise serializers.ValidationError(
                TASK_TITLE_TOO_LONG_ERROR
            )
        if len(description) > 1500:
            raise serializers.ValidationError(
                TASK_DESCRIPTION_TOO_LONG_ERROR
            )
        if isinstance(deadline, datetime.date) and (
                deadline < datetime.date.today() or deadline < data.get("date_started")
        ):
            raise serializers.ValidationError(
                WRONG_DEADLINE_ERROR
            )

        return data
