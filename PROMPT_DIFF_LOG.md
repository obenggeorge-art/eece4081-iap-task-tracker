# Prompt-and-Diff Log

## IAP-M1

### AI Tool Used

ChatGPT

### Purpose

I used ChatGPT as a learning and development aid while setting up my EECE 4081 Individual Application Project. I used it to understand the milestone requirements, select an appropriately sized application concept, set up the Python and Django development environment, organize the README, and verify the required development tools.

### Prompt Summary

I provided the IAP-M1 assignment requirements and asked ChatGPT to guide me through completing the milestone from scratch.

### Suggestions Received

The AI suggested using a Student Task Tracker as the project concept and recommended Python, Django, SQLite, pip, pytest, and Git as the development stack. It also provided guidance for creating the virtual environment, configuring pytest, creating the `.gitignore`, and organizing the README.

### Changes Accepted

I reviewed the suggestions and used the parts that matched the assignment requirements and my development environment.

### Verification

I manually executed the setup commands on my computer. I verified that Python and Django run correctly, started the Django development server, opened the application in a browser, and executed an automated test using pytest. I reviewed the files before adding them to version control.
### AI Tool Verification

**Tool:** GitHub Copilot Chat in Visual Studio Code

**Prompt:**
"Explain what the test_toolchain_is_working function in tasks/tests.py does. Do not modify any files."

**Response Summary:**
GitHub Copilot explained that the function is a simple sanity-check test used to verify that pytest, Python, and the project's test environment are working correctly. It also explained that the test checks whether 1 + 1 equals 2 and does not test the actual task-tracker application logic.

**Diff:**
No code changes were made from this prompt. The AI tool was used only to explain the existing test.

**Verification:**
GitHub Copilot Chat successfully responded inside Visual Studio Code.


---

## IAP-M2 — Requirements and AI Elicitation Audit

### Prompt Summary

For IAP-M2, I first developed the requirements for the Student Task Tracker, including eight user stories with acceptance criteria and three testable non-functional requirements.

I then used GitHub Copilot Chat as a separate AI elicitation tool and asked it to generate requirements based only on the original Student Task Tracker concept.

### AI Elicitation Prompt

**Tool:** GitHub Copilot Chat in Visual Studio Code

**Prompt:**

"I am developing a Student Task Tracker for my EECE 4081 Individual Application Project.

The application is a small web application for students to organize academic work in one place. A student should be able to create tasks for assignments, exams, projects, and other school responsibilities. Each task can have a due date and priority. Students should also be able to mark tasks as completed and view pending and completed tasks.

Based only on this description, elicit the software requirements for the application.

Provide:
1. Functional requirements or user stories with acceptance criteria.
2. Non-functional requirements.
3. Any additional requirements that you think the application should have.

Do not modify any project files. Only provide your proposed requirements in the chat."

### AI Response Summary

GitHub Copilot proposed six functional requirements covering task creation, due dates and priorities, pending tasks, completed tasks, completion status, and task types.

It also proposed non-functional requirements related to usability, accessibility, data integrity, reliability, privacy and security, compatibility, performance, and maintainability.

Copilot additionally suggested features such as editing, deleting, undoing completion, sorting and filtering, task notes, persistence, data retention, and possible student accounts.

### Diff — What I Changed or Rejected

I did not copy the AI-generated requirements directly into my final requirements document.

My final requirements differ from the AI response in several ways:

- I used eight user stories instead of the six functional requirements proposed by the AI.
- Editing a task is a definite requirement in my version rather than an optional suggestion.
- Deleting a task with confirmation is a definite requirement in my version.
- I defined the priority levels as Low, Medium, and High.
- I defined unfinished tasks with past due dates as overdue.
- I rejected additional features such as undo completion, sorting and filtering, task notes, data export, and student accounts because they are outside my current project scope.
- I replaced vague non-functional requirements with three requirements that have measurable or named verification conditions.
- Performance is defined as displaying the task list within 2 seconds with up to 500 tasks.
- Reliability requires saved task information to remain available after the application is restarted.
- Compatibility specifically requires the latest stable versions of Google Chrome, Microsoft Edge, and Mozilla Firefox.

### Useful AI Suggestions

The AI identified some ideas that I had not clearly considered, including empty states when no tasks are available, input validation, and accessibility considerations. I considered these useful ideas, but I did not automatically add every suggestion to the project requirements.

### Files Added or Changed

- Added `REQUIREMENTS.md`
- Added `AI_ELICITATION_AUDIT.md`
- Updated `PROMPT_DIFF_LOG.md`

### Verification

The final requirements were manually compared with the GitHub Copilot response. The differences, omissions, inventions, and useful AI suggestions are documented in `AI_ELICITATION_AUDIT.md`.