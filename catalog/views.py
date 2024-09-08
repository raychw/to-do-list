from django.urls import reverse_lazy
from django.views import generic


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"  # Your template
    context_object_name = "tasks"
