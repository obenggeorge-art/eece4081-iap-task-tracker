
import json
import logging
import uuid
from datetime import datetime, timezone

from django.shortcuts import render, redirect
from .models import Task


class JSONFormatter(logging.Formatter):
    """Format application events as structured JSON."""

    def format(self, record):
        log_data = {
            "timestamp": datetime.fromtimestamp(
                record.created, timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "event": record.getMessage(),
            "request_id": getattr(record, "request_id", None),
        }

        if hasattr(record, "task_id"):
            log_data["task_id"] = record.task_id

        return json.dumps(log_data)


logger = logging.getLogger("tasks")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)

logger.propagate = False


def create_task_from_post(post_data, request_id=None):
    """Create a task when all required form fields are present."""
    title = post_data.get("title")
    task_type = post_data.get("type")
    due_date = post_data.get("dueDate")
    priority = post_data.get("priority")

    logger.info(
        "task_validation_started",
        extra={"request_id": request_id},
    )

    if title and task_type and due_date and priority:
        task = Task.objects.create(
            title=title,
            type=task_type,
            dueDate=due_date,
            priority=priority,
            isCompleted=False,
        )

        logger.info(
            "task_created",
            extra={"request_id": request_id, "task_id": task.id},
        )
    else:
        logger.warning(
            "task_validation_failed",
            extra={"request_id": request_id},
        )


def task_list(request):
    if request.method == "POST":
        request_id = str(uuid.uuid4())

        logger.info(
            "task_create_started",
            extra={"request_id": request_id},
        )

        create_task_from_post(request.POST, request_id)

        logger.info(
            "task_create_completed",
            extra={"request_id": request_id},
        )

        return redirect("task_list")

    tasks = Task.objects.all().order_by("dueDate")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks},
    )
