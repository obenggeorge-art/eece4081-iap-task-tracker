
from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task_type = request.POST.get("type")
        due_date = request.POST.get("dueDate")
        priority = request.POST.get("priority")

        if title and task_type and due_date and priority:
            Task.objects.create(
                title=title,
                type=task_type,
                dueDate=due_date,
                priority=priority,
                isCompleted=False
            )

            return redirect("task_list")

    tasks = Task.objects.all().order_by("dueDate")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks}
    )
