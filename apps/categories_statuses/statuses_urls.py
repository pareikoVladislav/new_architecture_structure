from django.urls import path

from apps.categories_statuses.controllers.status_controllers import (
    ListStatusesAPIView,
    RetrieveStatusAPIView
)


urlpatterns = [
    path("", ListStatusesAPIView.as_view()),
    path("<int:status_id>/", RetrieveStatusAPIView.as_view()),
]
