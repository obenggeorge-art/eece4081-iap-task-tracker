def test_toolchain_is_working():
    assert 1 + 1 == 2


from datetime import date
from django.test import TestCase
from .models import Task


def test_toolchain_is_working():
    assert 1 + 1 == 2


class TaskDatabaseTest(TestCase):

    def test_create_and_retrieve_task(self):
        Task.objects.create(
            title="EECE 4081 Assignment",
            type="Assignment",
            dueDate=date(2026, 10, 20),
            priority="High",
            isCompleted=False
        )

        saved_task = Task.objects.get(
            title="EECE 4081 Assignment"
        )

        self.assertEqual(saved_task.type, "Assignment")
        self.assertEqual(saved_task.priority, "High")
        self.assertFalse(saved_task.isCompleted)
