from django import forms

from catalog.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    deadline = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local"
        })
    )
