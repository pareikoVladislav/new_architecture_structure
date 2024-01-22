from apps.categories_statuses.repositories.category_repository import CategoryRepository
from apps.categories_statuses.serializers import CategorySerializer


class CategoryService:
    """
    Service class for handling business logic related to
    Category entities.

    This class provides methods to manage Category instances,
    utilizing CategoryRepository for database operations
    and CategorySerializer for data serialization.

    Attributes:
        category_repo (CategoryRepository): Repository instance
        for database operations.
        serializer (CategorySerializer): Serializer class for
        category data serialization.
    """
    category_repo = CategoryRepository()
    serializer = CategorySerializer

    def get_all_categories(self):
        """
        Retrieves all categories and returns them in serialized format.

        Returns:
            list: A list of serialized category data.
        """
        categories = self.category_repo.get_all()
        serializer = self.serializer(categories, many=True)

        return serializer.data

    def get_category_by_pk(self, pk):
        """
        Retrieves a category by its primary key and returns
        it in serialized format.

        Args:
            pk (int): The primary key of the category.

        Returns:
            dict: Serialized data of the requested category.
        """
        category = self.category_repo.get_by_pk(pk=pk)
        serializer = self.serializer(category)

        return serializer.data

    def get_category_by_name(self, name):
        """
        Retrieves a category by its name and returns it
        in serialized format.

        Args:
            name (str): The name of the category.

        Returns:
            dict: Serialized data of the requested category.
        """
        category = self.category_repo.get_by_name(name=name)
        serializer = self.serializer(category)

        return serializer.data

    def create_new_category(self, data):
        """
        Creates a new category from the given data.

        Args:
            data (dict): Data for creating a new category.

        Returns:
            dict: Serialized data of the newly created category,
            or validation errors if the data is invalid.
        """
        serializer = self.serializer(data=data)

        if serializer.is_valid(raise_exception=True):

            validated_data = serializer.validated_data
            category = self.category_repo.create_category(
                validated_data=validated_data
            )

            return self.serializer(category).data

        else:
            return serializer.errors

    def update_category_by_pk(self, category_id, data):
        """
        Updates a category identified by its primary key
        with the given data.

        Args:
            category_id (int): The primary key of the category
            to be updated.
            data (dict): Data for updating the category.

        Returns:
            dict: Serialized data of the updated category, or
            validation errors if the data is invalid.
        """
        category = self.category_repo.get_by_pk(category_id)
        serializer = self.serializer(category, data=data)

        if serializer.is_valid():

            updated_category = self.category_repo.update_category(
                category=category,
                validated_data=serializer.validated_data
            )

            return self.serializer(updated_category).data

        else:
            return serializer.errors

    def delete_category_by_id(self, category_id):
        """
        Deletes a category identified by its primary key.

        Args:
            category_id (int): The primary key of the category
            to be deleted.
        """
        category = self.category_repo.get_by_pk(pk=category_id)
        category.delete()
