from django.urls import path, include


urlpatterns = [
    path("categories/", include('apps.categories_statuses.categories_urls')),
    path("statuses/", include('apps.categories_statuses.statuses_urls')),
    path("tasks/", include('apps.tasks.urls')),
    # path("subtasks/", include('apps.subtasks.urls')),
    # path("user/", include('apps.user.urls')),
]
