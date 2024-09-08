from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "catalog/index.html"  # Your template
    context_object_name = "task_list"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 10
