
from django.shortcuts import render, redirect
from .models import Task


def create_task_from_post(post_data):
    """Create a task when all required form fields are present."""
    title = post_data.get("title")
    task_type = post_data.get("type")
    due_date = post_data.get("dueDate")
    priority = post_data.get("priority")

    if title and task_type and due_date and priority:
        Task.objects.create(
            title=title,
            type=task_type,
            dueDate=due_date,
            priority=priority,
            isCompleted=False,
        )


def task_list(request):
    if request.method == "POST":
        create_task_from_post(request.POST)
        return redirect("task_list")

    tasks = Task.objects.all().order_by("dueDate")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks},
    )
