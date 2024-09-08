from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "catalog/index.html"  # Your template
    context_object_name = "tasks"


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"
