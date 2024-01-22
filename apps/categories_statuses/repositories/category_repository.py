from rest_framework.generics import get_object_or_404

from apps.categories_statuses.models import Category


class CategoryRepository:
    """
    Repository class for handling database operations
    related to Category model.

    This class provides an abstraction layer over Django's
    ORM for Category model operations.
    """
    def get_all(self):
        """
        Retrieves all category instances from the database.

        Returns:
            QuerySet: A Django QuerySet containing all
            Category instances.
        """
        return Category.objects.all()

    def get_by_pk(self, pk):
        """
        Retrieves a single category instance by its primary key (pk).

        Args:
            pk (int): The primary key of the category to be retrieved.

        Returns:
            Category: The Category instance corresponding to the given pk.

        Raises:
            Http404: If no Category instance with the given pk is found.
        """
        return get_object_or_404(Category, id=pk)

    def get_by_name(self, name):
        """
        Retrieves a single category instance by its name.

        Args:
            name (str): The name of the category to be retrieved.

        Returns:
            Category: The Category instance corresponding to the given name.

        Raises:
            Http404: If no Category instance with the given name is found.
        """
        return get_object_or_404(Category, name=name)

    def create_category(self, validated_data):
        """
        Creates a new category instance with the given validated data.

        Args:
            validated_data (dict): A dictionary containing data
            to create a new Category instance.

        Returns:
            Category: The newly created Category instance.
        """
        category = Category.objects.create(**validated_data)

        return category

    def update_category(self, category, validated_data):
        """
        Updates an existing category instance with the given
        validated data.

        Args:
            category (Category): The Category instance to update.
            validated_data (dict): A dictionary containing data to
            update the Category instance.

        Returns:
            Category: The updated Category instance.
        """
        for key, value in validated_data.items():
            setattr(category, key, value)
        category.save()

        return category
