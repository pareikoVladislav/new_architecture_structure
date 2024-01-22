from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from apps.categories_statuses.services.category_services import CategoryService
from apps.categories_statuses.success_messages import (
    CATEGORY_SUCCESS_DELETING_MESSAGE,
)


class ListCategoriesAPIView(APIView):
    """
    API view for listing and creating categories.

    Attributes:
        service (CategoryService): An instance of CategoryService
        for handling category-related operations.
    """
    service = CategoryService()

    def get(self, request: Request, *args, **kwargs):
        """
        Handles GET requests to list all categories.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A Response object with HTTP status 200 and
            a list of categories in its data.
        """
        categories_data = self.service.get_all_categories()

        return Response(
            status=status.HTTP_200_OK,
            data=categories_data
        )

    def post(self, request: Request, *args, **kwargs):
        """
        Handles POST requests to create a new category.

        Args:
            request (Request): The incoming HTTP request containing
            the data for the new category.

        Returns:
            Response: A Response object with HTTP status 201 and
            the created category data.
        """
        new_category = self.service.create_new_category(
            data=request.data
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=new_category
        )


class RetrieveCategoryAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a
    specific category.

    Attributes:
        service (CategoryService): An instance of CategoryService
        for handling category-related operations.
    """
    service = CategoryService()

    def get(self, request: Request, *args, **kwargs):
        """
        Handles GET requests to retrieve a specific category.

        Args:
            request (Request): The incoming HTTP request.
            kwargs: Keyword arguments containing 'category_id'.

        Returns:
            Response: A Response object with HTTP status 200 and
            the requested category's data, if found.
        """
        category_id = kwargs.get("category_id")

        if category_id:
            category = self.service.get_category_by_pk(
                pk=category_id
            )
            return Response(
                status=status.HTTP_200_OK,
                data=category
            )

    def put(self, request: Request, *args, **kwargs):
        """
        Handles PUT requests to update a specific category.

        Args:
            request (Request): The incoming HTTP request containing update data.
            kwargs: Keyword arguments containing 'category_id'.

        Returns:
            Response: A Response object with HTTP status 202 if update is successful,
                      or HTTP status 400/500 with error details in case of failure.
        """
        category_id = kwargs.get("category_id")

        if not category_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "error": "Category 'pk' not provided."
                }
            )

        try:
            result = self.service.update_category_by_pk(
                category_id=category_id,
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
        Handles DELETE requests to delete a specific category.

        Args:
            request (Request): The incoming HTTP request.
            kwargs: Keyword arguments containing 'category_id'.

        Returns:
            Response: A Response object with HTTP status 200 and a
            success message upon successful deletion.
        """
        category_id = kwargs.get("category_id")

        if category_id:
            self.service.delete_category_by_id(
                category_id=category_id
            )
            return Response(
                status=status.HTTP_200_OK,
                data=CATEGORY_SUCCESS_DELETING_MESSAGE
            )
