from django.urls import path

from catalog.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_complete_to_task,
    TagListView,
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="index"
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "<int:pk>/toggle-complete/",
        toggle_complete_to_task,
        name="task-toggle-complete"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
]

app_name="catalog"
