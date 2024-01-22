from apps.categories_statuses.repositories.status_repository import (
    StatusRepository,
)
from apps.categories_statuses.serializers import StatusSerializer


class StatusService:
    status_repo = StatusRepository()
    serializer = StatusSerializer

    def get_all_statuses(self):
        statuses = self.status_repo.get_all()
        serializer = self.serializer(statuses, many=True)

        return serializer.data

    def get_status_by_pk(self, pk):
        status = self.status_repo.get_by_pk(pk=pk)
        serializer = self.serializer(status)

        return serializer.data

    def get_status_by_name(self, name):
        status = self.status_repo.get_by_name(name=name)
        serializer = self.serializer(status)

        return serializer.data

    def create_new_status(self, data):
        serializer = self.serializer(data=data)

        if serializer.is_valid(raise_exception=True):

            validated_data = serializer.validated_data
            status = self.status_repo.create_status(
                validated_data=validated_data
            )

            return self.serializer(status).data

        else:
            return serializer.errors

    def update_status_by_pk(self, status_id, data):
        status = self.status_repo.get_by_pk(status_id)
        serializer = self.serializer(status, data=data)

        if serializer.is_valid():

            updated_category = self.status_repo.update_status(
                status_obj=status,
                validated_data=serializer.validated_data
            )

            return self.serializer(updated_category).data

        else:
            return serializer.errors

    def delete_status_by_id(self, status_id):
        status = self.status_repo.get_by_pk(pk=status_id)
        status.delete()
