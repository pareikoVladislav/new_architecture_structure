from django.urls import path

from apps.categories_statuses.controllers.category_controllers import (
    ListCategoriesAPIView,
    RetrieveCategoryAPIView
)


urlpatterns = [
    path("", ListCategoriesAPIView.as_view()),
    path("<int:category_id>/", RetrieveCategoryAPIView.as_view()),
]
