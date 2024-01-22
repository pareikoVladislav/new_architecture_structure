from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from apps.categories_statuses.services.status_services import (
    StatusService,
)
from apps.categories_statuses.success_messages import (
    STATUS_SUCCESS_DELETING_MESSAGE,
)


class ListStatusesAPIView(APIView):
    """
    API view for listing and creating status entities.

    This view handles requests for retrieving all status
    records and creating new ones.

    Attributes:
        service (StatusService): An instance of StatusService
        for handling status-related operations.
    """
    service = StatusService()

    def get(self, request: Request, *args, **kwargs):
        """
        Handles GET requests to retrieve a list of all statuses.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A Response object with HTTP status 200 and
            serialized data of all statuses.
        """
        statuses_data = self.service.get_all_statuses()

        return Response(
            status=status.HTTP_200_OK,
            data=statuses_data
        )

    def post(self, request: Request, *args, **kwargs):
        """
        Handles POST requests to create a new status.

        Args:
            request (Request): The incoming HTTP request containing
            the data for the new status.

        Returns:
            Response: A Response object with HTTP status 201 and
            serialized data of the created status.
        """
        new_status = self.service.create_new_status(
            data=request.data
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=new_status
        )


class RetrieveStatusAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a
    specific status entity.

    This view handles requests for managing a single
    status record identified by its primary key.

    Attributes:
        service (StatusService): An instance of StatusService
        for handling status-related operations.
    """
    service = StatusService()

    def get(self, request: Request, *args, **kwargs):
        """
        Handles GET requests to retrieve a specific status by its ID.

        Args:
            request (Request): The incoming HTTP request.
            kwargs: Keyword arguments containing 'status_id'.

        Returns:
            Response: A Response object with HTTP status 200 and
            serialized data of the requested status.
        """
        status_id = kwargs.get("status_id")

        if status_id:
            status_obj = self.service.get_status_by_pk(
                pk=status_id
            )
            return Response(
                status=status.HTTP_200_OK,
                data=status_obj
            )

    def put(self, request: Request, *args, **kwargs):
        """
        Handles PUT requests to update a specific status by its ID.

        Args:
            request (Request): The incoming HTTP request
            containing updated data.
            kwargs: Keyword arguments containing 'status_id'.

        Returns:
            Response: A Response object with HTTP status 202 and
            serialized data of the updated status,
            or with error details in case of failure.
        """
        status_id = kwargs.get("status_id")

        try:
            result = self.service.update_status_by_pk(
                status_id=status_id,
                data=request.data
            )

            return Response(
                status=status.HTTP_202_ACCEPTED,
                data=result
            )
        except ValidationError as err:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=err.detail
            )
        except Exception as err:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=str(err)
            )

    def delete(self, request: Request, *args, **kwargs):
        """
        Handles DELETE requests to remove a specific status by its ID.

        Args:
            request (Request): The incoming HTTP request.
            kwargs: Keyword arguments containing 'status_id'.

        Returns:
            Response: A Response object with HTTP status 200 and a
            success message upon successful deletion.
        """
        status_id = kwargs.get("status_id")

        if status_id:
            self.service.delete_status_by_id(
                status_id=status_id
            )
            return Response(
                status=status.HTTP_200_OK,
                data=STATUS_SUCCESS_DELETING_MESSAGE
            )
