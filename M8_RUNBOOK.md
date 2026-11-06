# M8 Runbook — Task Not Appearing After Submission

**Application:** Student Task Tracker
**Severity:** Medium
**Affected feature:** Task creation
**Purpose:** Help another developer diagnose and resolve a task submission problem.

## 1. Observable Symptom

A student fills out the task creation form and clicks Submit. The application redirects to the task list, but the new task does not appear.

The application may continue running without showing an error message.

## 2. Confirm the Problem

1. Open the Student Task Tracker application.
2. Enter a task title, type, due date, and priority.
3. Submit the form.
4. Check whether the task appears in the list.
5. If it does not appear, open the terminal running the Django server.

Look for JSON log records containing these events:

- `task_create_started`
- `task_validation_started`
- `task_created`
- `task_validation_failed`
- `task_create_completed`

Use the `request_id` field to identify records belonging to the same submission.

## 3. Diagnose the Failure

**Case A — Validation failed**

If the logs contain `task_validation_failed`, the application did not receive all required form fields.

Check that the submitted form includes:

- `title`
- `type`
- `dueDate`
- `priority`

Inspect `tasks/templates/tasks/task_list.html` and confirm that the input names match the field names expected in `tasks/views.py`.

**Case B — Task was created but is not displayed**

If the logs contain `task_created`, the database creation operation completed.

Check the task list query in `tasks/views.py`:

`Task.objects.all().order_by("dueDate")`

Confirm that the task list template displays the returned tasks.

**Case C — No structured logs appear**

Confirm that the Django server is running and that the form submits a POST request to the correct application route.

Check the server terminal for startup errors or request failures.

## 4. Recovery Procedure

1. Correct any missing or mismatched form field names.
2. Confirm that the database is available and migrations have been applied.
3. If needed, run:

   `python manage.py migrate`

4. Restart the development server:

   `python manage.py runserver`

5. Submit a new test task.

Do not delete the database or existing tasks during troubleshooting.

## 5. Verify Recovery

The issue is resolved when:

1. The submitted task appears in the task list.
2. The logs contain `task_created`.
3. The `task_create_started`, `task_validation_started`, `task_created`, and `task_create_completed` events share the same `request_id`.
4. Existing automated tests pass using:

   `python manage.py test tasks -v 2`

Expected result: All six existing tests pass.

## 6. Escalation

If the task still does not appear, collect:

- The approximate time of the failed submission.
- The related JSON log records and `request_id`.
- Any Django error messages.
- The results of the automated tests.

Share this information with the project maintainer for further investigation. Avoid sharing passwords or other sensitive form data.