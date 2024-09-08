from django.urls import path

from catalog.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index")
]

app_name="catalog"
