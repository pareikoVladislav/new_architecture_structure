from rest_framework.generics import get_object_or_404

from apps.categories_statuses.models import Status


class StatusRepository:
    def get_all(self):
        return Status.objects.all()

    def get_by_pk(self, pk):
        return get_object_or_404(Status, id=pk)

    def get_by_name(self, name):
        return get_object_or_404(Status, name=name)

    def create_status(self, validated_data):
        category = Status.objects.create(**validated_data)

        return category

    def update_status(self, status_obj, validated_data):
        for key, value in validated_data.items():
            setattr(status_obj, key, value)
        status_obj.save()

        return status_obj
