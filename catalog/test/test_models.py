from django.test import TestCase
from datetime import datetime

from catalog.models import Task, Tag


class TagModelTests(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Work")
        self.assertEqual(tag.name, "Work")
        self.assertEqual(str(tag), "Work")

class TaskModelTests(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

    def test_task_creation(self):
        task = Task.objects.create(
            content="Test Task",
            deadline=datetime(2024, 12, 31, 23, 59),
            is_done=False
        )
        self.assertEqual(task.content, "Test Task")
        self.assertEqual(task.deadline, datetime(2024, 12, 31, 23, 59))
        self.assertFalse(task.is_done)
        self.assertIsNotNone(task.datetime)
        self.assertEqual(str(task), "Test Task")

    def test_task_tags(self):
        task = Task.objects.create(
            content="Task with Tags",
            deadline=datetime(2024, 12, 31, 23, 59),
            is_done=False
        )
        task.tags.add(self.tag1, self.tag2)
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())

    def test_ordering(self):
        task1 = Task.objects.create(content="Task 1", is_done=True)
        task2 = Task.objects.create(content="Task 2", is_done=False, datetime=datetime(2024, 1, 1))
        task3 = Task.objects.create(content="Task 3", is_done=False, datetime=datetime(2024, 1, 2))

        tasks = Task.objects.all()
        self.assertEqual(list(tasks), [task3, task2, task1])
