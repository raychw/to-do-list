from django.urls import path

from catalog.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name="catalog"
