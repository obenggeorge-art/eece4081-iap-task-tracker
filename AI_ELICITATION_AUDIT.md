# AI Elicitation Audit

## IAP M2 — Requirements and AI Elicitation Audit

### Project

Student Task Tracker

### AI Tool Used

GitHub Copilot Chat in Visual Studio Code

## Prompt Given to the AI

I am developing a Student Task Tracker for my EECE 4081 Individual Application Project.

The application is a small web application for students to organize academic work in one place. A student should be able to create tasks for assignments, exams, projects, and other school responsibilities. Each task can have a due date and priority. Students should also be able to mark tasks as completed and view pending and completed tasks.

Based only on this description, elicit the software requirements for the application.

Provide:
1. Functional requirements or user stories with acceptance criteria.
2. Non-functional requirements.
3. Any additional requirements that you think the application should have.

Do not modify any project files. Only provide your proposed requirements in the chat.

## Summary of the AI Response

The AI produced six functional requirements with user stories and acceptance criteria. It covered creating tasks, setting due dates and priorities, viewing pending tasks, marking tasks as completed, viewing completed tasks, and distinguishing task types.

It also suggested non-functional requirements for usability, accessibility, data integrity, reliability, privacy and security, compatibility, performance, and maintainability.

Finally, it suggested additional requirements such as editing and deleting tasks, data persistence, undoing completion, defining priority levels, overdue behavior, sorting and filtering, task descriptions, data retention, and possible user accounts.

## What the AI Got Right

The AI correctly identified the main functions from the project description. It included creating tasks, assigning due dates and priorities, viewing pending tasks, marking tasks as completed, and viewing completed tasks. These match the main purpose of my Student Task Tracker.

The AI also correctly recognized that task type should be represented in the system. It suggested assignment, exam, project, and other as possible task types.

One useful idea that I had not clearly considered was showing an empty state when there are no pending or completed tasks. This would make the interface clearer instead of displaying an empty page without explanation.

The AI also raised useful questions about invalid input and accessibility. For example, it suggested giving a clear indication when required information is missing or invalid and making controls keyboard-operable. These are useful considerations even though they were not part of my original project description.

## What the AI Missed

The AI missed several specific decisions that are included in my requirements.

First, it did not make editing an existing task a definite functional requirement. It only said, "If the application supports editing," and later listed editing under additional requirements. My requirements specifically allow the student to edit an existing task and change its title, type, due date, and priority.

Second, it did not make deleting a task a definite functional requirement. It only recommended deletion as an additional requirement. My requirements include deleting an existing task and asking the student for confirmation before the deletion occurs.

Third, the AI did not define the priority levels that my requirements use. My requirements specifically use Low, Medium, and High. The AI instead said that the available priority levels should be decided.

Fourth, the AI did not specify my overdue-task behavior as a requirement. My requirements state that a task with a past due date that has not been completed should be identified as overdue. The AI only raised overdue behavior as something to consider.

The AI also missed the measurable conditions in my non-functional requirements. For example, my performance requirement states that the task list must be displayed within 2 seconds with up to 500 tasks. The AI only said that common actions should complete "promptly," which cannot be objectively tested because it does not define a time limit.

My compatibility requirement names the latest stable versions of Google Chrome, Microsoft Edge, and Mozilla Firefox. The AI only said that the application should work on the browsers and device sizes targeted by the project without naming those browsers.

My reliability requirement also gives a specific test condition: saved task information must still be available after the application is restarted. The AI discussed reliability but did not clearly require persistence after a restart.

## What the AI Invented

The AI introduced several requirements that were not stated in my original project concept and that I had not chosen as requirements.

It suggested an undo-completion feature that would allow a completed task to return to pending. I did not request this feature.

It suggested sorting and filtering tasks by due date, priority, task type, or completion status. My current project does not require sorting or filtering.

It suggested adding an optional task description or notes field for instructions, course information, or links. I did not include a description or notes field in my requirements.

It also introduced the possibility of student accounts, remote storage, authorization, and data isolation between students. My current project description does not require a login system or multiple student accounts.

The AI suggested data export, clearing stored data, and defining data-retention behavior. These were also not part of my planned Student Task Tracker.

These suggestions are not necessarily bad features, but accepting them automatically would increase the scope of the project beyond the requirements I selected.

## Comparison of Non-Functional Requirements

The AI identified several useful non-functional requirement categories, but most of them were too general to satisfy the milestone requirement that an NFR must be falsifiable.

For example, saying that common actions should complete "promptly" does not provide a measurable performance threshold. Saying that the application should work on targeted browsers also does not identify which browsers must be tested.

My NFRs are more specific because they define measurable or named test conditions. Performance has a 2-second limit with up to 500 tasks. Reliability is tested by restarting the application and checking whether saved information remains available. Compatibility names Google Chrome, Microsoft Edge, and Mozilla Firefox and defines the operations that must work.

## Overall Judgment

The AI response was useful as a starting point, but I would not use it as the final requirements document without reviewing and changing it. It correctly found most of the basic functions in the project description and raised some useful issues, especially input validation, empty states, and accessibility.

However, it treated some functions that I selected for my project, such as editing and deleting tasks, as optional suggestions instead of definite requirements. It also introduced features such as accounts, sorting and filtering, notes, undo completion, and data export that I did not request. Accepting all of these suggestions would increase the project scope.

The biggest weakness was the non-functional requirements. Most of the AI-generated NFRs used general words such as "straightforward," "promptly," and "targeted" without measurable thresholds or clearly named test conditions. For this project, I kept the useful ideas from the AI in mind but used my own more specific and testable requirements as the final requirements.