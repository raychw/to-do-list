from django import forms

from catalog.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local"
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
