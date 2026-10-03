# Student Task Tracker — Requirements

## IAP M2 — Requirements and AI Elicitation Audit

## Project Overview

The Student Task Tracker is a web application designed to help students organize their academic work in one place. A user will be able to create tasks for assignments, exams, projects, and other school responsibilities, assign a due date and priority to each task, and mark tasks as completed. The application will also allow the student to view pending and completed tasks so that it is easier to keep track of upcoming work.

## User Stories

### US-01 — Create a Task

As a student,
I want to create a task for my schoolwork,
so that I can keep track of work that I need to complete.

**Acceptance Criteria:**
- The student can enter a title for the task.
- The student can select the type of task, such as an assignment, exam, or project.
- The student can assign a due date to the task.
- The student can assign a priority to the task.
- The task is saved after the student submits it.
- The saved task appears in the student's task list.

### US-02 — View Pending Tasks

As a student,
I want to view my pending tasks,
so that I can see the schoolwork that I still need to complete.

**Acceptance Criteria:**
- The student can view a list of pending tasks.
- Each pending task displays its title, due date, and priority.
- Tasks marked as completed do not appear in the pending task list.
- A newly created task appears in the pending task list until it is completed.

### US-03 — View Completed Tasks

As a student,
I want to view my completed tasks,
so that I can keep track of the schoolwork that I have already finished.

**Acceptance Criteria:**
- The student can view a list of completed tasks.
- Each completed task displays its title, due date, and priority.
- Only tasks marked as completed appear in the completed task list.
- A task appears in the completed task list after it is marked as completed.

### US-04 — Mark a Task as Completed

As a student,
I want to mark a task as completed,
so that I can separate finished work from work that I still need to complete.

**Acceptance Criteria:**
- The student can mark a pending task as completed.
- The completed status is saved by the application.
- The task no longer appears in the pending task list after it is completed.
- The task appears in the completed task list after it is completed.

### US-05 — Edit a Task

As a student,
I want to edit an existing task,
so that I can correct or update my schoolwork information.

**Acceptance Criteria:**
- The student can select an existing task to edit.
- The student can change the task title, type, due date, and priority.
- The student can save the updated task.
- The updated information appears in the task list after it is saved.

### US-06 — Delete a Task

As a student,
I want to delete a task,
so that I can remove schoolwork that I no longer need to track.

**Acceptance Criteria:**
- The student can select an existing task to delete.
- The application asks the student to confirm the deletion.
- The task is removed after the student confirms the deletion.
- The deleted task no longer appears in the pending or completed task lists.

### US-07 — Prioritize Tasks

As a student,
I want to assign a priority to my tasks,
so that I can identify which schoolwork needs my attention first.

**Acceptance Criteria:**
- The student can assign a priority when creating or editing a task.
- The available priority levels are Low, Medium, and High.
- The selected priority is saved with the task.
- The priority level is displayed when the student views the task.

### US-08 — Track Due Dates

As a student,
I want to assign and view due dates for my tasks,
so that I can know when my schoolwork needs to be completed.

**Acceptance Criteria:**
- The student can assign a due date when creating or editing a task.
- The selected due date is saved with the task.
- The due date is displayed when the student views the task.
- Tasks with past due dates that are not completed are identified as overdue.

## Non-Functional Requirements

### NFR-01 — Performance

Under normal use, the application shall display the task list within 2 seconds after the student requests the page when the database contains up to 500 tasks.

**Verification:** Measure the time between requesting the task list and the completed page response using a test database containing 500 tasks. The requirement passes if the response takes 2 seconds or less.

### NFR-02 — Reliability

When a student successfully creates, edits, or changes the completion status of a task, the saved information shall still be available after the application is restarted.

**Verification:** Create or modify a task, restart the application, and retrieve the task again. The requirement passes if the saved information remains unchanged.

### NFR-03 — Browser Compatibility

The application shall support the latest stable versions of Google Chrome, Microsoft Edge, and Mozilla Firefox without preventing the student from creating, viewing, editing, deleting, or completing a task.

**Verification:** Perform the main task operations in each of the three named browsers. The requirement passes if all listed operations can be completed successfully in each browser.