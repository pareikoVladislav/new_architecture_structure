from rest_framework import serializers

from apps.categories_statuses.models import (
    Category,
    Status,
)
from apps.categories_statuses.validate_err_messages import (
    CATEGORY_NAME_MAX_LENGTH_ERROR,
    CATEGORY_NAME_MIN_LENGTH_ERROR,
    CATEGORY_NAME_TYPE_ERROR,
    STATUS_NAME_MAX_LENGTH_ERROR,
    STATUS_NAME_MIN_LENGTH_ERROR,
    STATUS_NAME_TYPE_ERROR,
)


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Category model.

    This serializer handles serialization and deserialization
    of Category instances,
    along with custom validation for the 'name' field.

    Attributes:
        Meta: An inner class defining model and fields to
        be serialized.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        """
         Validates the 'name' field of the Category.

         Args:
             value (str): The value of the 'name' field to validate.

         Returns:
             str: The validated 'name' field.

         Raises:
             serializers.ValidationError: If the 'name' does not meet
             the length or type requirements.
         """
        if value is None:
            return value
        if len(value) > 25:
            raise serializers.ValidationError(CATEGORY_NAME_MAX_LENGTH_ERROR)
        if len(value) < 4:
            raise serializers.ValidationError(CATEGORY_NAME_MIN_LENGTH_ERROR)
        if not isinstance(value, str):
            raise serializers.ValidationError(CATEGORY_NAME_TYPE_ERROR)

        return value


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Status model.

    This serializer handles serialization and deserialization
    of Status instances,
    along with custom validation for the 'name' field.

    Attributes:
        Meta: An inner class defining model and fields to be serialized.
    """
    class Meta:
        model = Status
        fields = ['id', 'name']

    def validate_name(self, value):
        """
        Validates the 'name' field of the Status.

        Args:
            value (str): The value of the 'name' field to validate.

        Returns:
            str: The validated 'name' field.

        Raises:
            serializers.ValidationError: If the 'name' does not meet
            the length or type requirements.
        """
        if value is None:
            return value
        if len(value) > 30:
            raise serializers.ValidationError(STATUS_NAME_MAX_LENGTH_ERROR)
        if len(value) < 3:
            raise serializers.ValidationError(STATUS_NAME_MIN_LENGTH_ERROR)
        if not isinstance(value, str):
            raise serializers.ValidationError(STATUS_NAME_TYPE_ERROR)

        return value
