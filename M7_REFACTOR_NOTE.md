# IAP M7 — Documented Refactor

## Code Smell: Mixed Responsibilities

In my Student Task Tracker application, the `task_list()` function in `tasks/views.py` was handling too many tasks. It read form data, checked required fields, created tasks in the database, and displayed the task list.

Although the application worked, having all these responsibilities in one function made the code harder to read and maintain.

## What I Changed

I extracted the task-creation logic into a separate helper function called `create_task_from_post()`.

The helper now reads the submitted form values, checks that the required fields are present, and creates the task in the database.

The `task_list()` function now focuses on handling HTTP requests, redirecting after submission, and displaying tasks.

I kept the same validation condition, task fields, redirect, and due-date ordering.

## How I Verified the Refactor

Before refactoring, I ran the six existing tests from M6. All six passed.

After refactoring, I ran the same test suite again without changing the tests. All six passed.

- Before: 6 tests passed.
- After: 6 tests passed.
- Result: No behavior changes were detected by the existing tests.

## What Became Easier

The code is now easier to understand because the task-creation logic is separated from the request-handling logic.

If I need to change how tasks are created in the future, I can focus on the helper function instead of searching through the entire view.

This refactor improves the internal organization of the application while preserving the behavior covered by the tests.