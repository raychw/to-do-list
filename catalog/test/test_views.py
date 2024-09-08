from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Task, Tag


class TaskViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

        self.task1 = Task.objects.create(
            content="Task 1",
            deadline=None,
            is_done=False
        )
        self.task2 = Task.objects.create(
            content="Task 2",
            deadline=None,
            is_done=True
        )
        self.task1.tags.add(self.tag1)
        self.task2.tags.add(self.tag2)

    def test_task_list_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_task_create_view(self):
        response = self.client.post(reverse("catalog:task-create"), {
            "content": "New Task",
            "deadline": "",
            "tags": [self.tag1.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_update_view(self):
        response = self.client.post(reverse("catalog:task-update", args=[self.task1.id]), {
            "content": "Updated Task",
            "deadline": "",
            "tags": [self.tag2.id]
        })
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.content, "Updated Task")
        self.assertIn(self.tag2, self.task1.tags.all())

    def test_task_delete_view(self):
        response = self.client.post(reverse("catalog:task-delete", args=[self.task1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())

    def test_toggle_complete_view(self):
        response = self.client.get(reverse("catalog:task-toggle-complete", args=[self.task1.id]))
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.is_done)


class TagViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

    def test_tag_list_view(self):
        response = self.client.get(reverse("catalog:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/tag_list.html")
        self.assertContains(response, "Work")
        self.assertContains(response, "Personal")

    def test_tag_create_view(self):
        response = self.client.post(reverse("catalog:tag-create"), {
            "name": "New Tag"
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_tag_update_view(self):
        response = self.client.post(reverse("catalog:tag-update", args=[self.tag1.id]), {
            "name": "Updated Tag"
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.tag1.refresh_from_db()
        self.assertEqual(self.tag1.name, "Updated Tag")

    def test_tag_delete_view(self):
        response = self.client.post(reverse("catalog:tag-delete", args=[self.tag1.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertFalse(Tag.objects.filter(id=self.tag1.id).exists())
