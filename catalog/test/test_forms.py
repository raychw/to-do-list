from django.test import TestCase

from catalog.models import Tag
from catalog.forms import TaskForm


class TaskFormTests(TestCase):

    def setUp(self):
        # Create some tags for testing
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

    def test_form_valid_data(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2024-12-31T23:59",
            "tags": [self.tag1.id, self.tag2.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.content, "Test Task")
        self.assertEqual(list(task.tags.all()), [self.tag1, self.tag2])

    def test_form_invalid_data(self):
        form_data = {
            "content": "",
            "deadline": "invalid date",
            "tags": []
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)
        self.assertIn("deadline", form.errors)

    def test_deadline_field(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2024-12-31T23:59",
            "tags": [self.tag1.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["deadline"].strftime("%Y-%m-%d %H:%M:%S"), "2024-12-31 23:59:00")

    def test_tags_field(self):
        form_data = {
            "content": "Test Task",
            "deadline": "",
            "tags": [self.tag1.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertIn(self.tag1, form.cleaned_data["tags"])
        self.assertNotIn(self.tag2, form.cleaned_data["tags"])
