
from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskAcceptanceTests(TestCase):

    def test_student_can_create_and_view_task(self):
        response = self.client.post(
            reverse("task_list"),
            {
                "title": "EECE 4081 Homework",
                "type": "Assignment",
                "dueDate": "2026-11-10",
                "priority": "High",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get(title="EECE 4081 Homework")

        self.assertEqual(task.type, "Assignment")
        self.assertEqual(task.dueDate, date(2026, 11, 10))
        self.assertEqual(task.priority, "High")
        self.assertFalse(task.isCompleted)

        self.assertContains(response, "EECE 4081 Homework")

    def test_tasks_appear_in_earliest_deadline_order(self):
        Task.objects.create(
            title="Later Assignment",
            type="Assignment",
            dueDate=date(2026, 11, 20),
            priority="Low",
        )

        Task.objects.create(
            title="Urgent Assignment",
            type="Assignment",
            dueDate=date(2026, 11, 5),
            priority="High",
        )

        response = self.client.get(reverse("task_list"))

        self.assertEqual(response.status_code, 200)

        tasks = list(response.context["tasks"])

        self.assertEqual(tasks[0].title, "Urgent Assignment")
        self.assertEqual(tasks[1].title, "Later Assignment")


class TaskModelTests(TestCase):

    def test_new_task_is_incomplete_by_default(self):
        task = Task(
            title="Study for Exam",
            type="Exam",
            dueDate=date(2026, 11, 12),
            priority="Medium",
        )

        self.assertFalse(task.isCompleted)

    def test_task_string_representation_is_title(self):
        task = Task(
            title="Finish Project",
            type="Project",
            dueDate=date(2026, 11, 15),
            priority="High",
        )

        self.assertEqual(str(task), "Finish Project")

    def test_task_type_choices(self):
        allowed_types = [
            value for value, label in Task.TASK_TYPES
        ]

        self.assertEqual(
            allowed_types,
            ["Assignment", "Exam", "Project", "Other"],
        )

    def test_priority_choices(self):
        allowed_priorities = [
            value for value, label in Task.PRIORITIES
        ]

        self.assertEqual(
            allowed_priorities,
            ["Low", "Medium", "High"],
        )
