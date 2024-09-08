from django.urls import path

from catalog.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name="catalog"
