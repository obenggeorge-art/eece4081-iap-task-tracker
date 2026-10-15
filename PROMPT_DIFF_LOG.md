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
## IAP M3 — Domain Model and AI Critique

### AI Tool Used
GitHub Copilot in Visual Studio Code.

### Prompt Given to AI
I asked GitHub Copilot to review my eight user stories and three non-functional requirements from IAP M2 and generate a domain-focused class diagram for my Student Task Tracker application.

I instructed the AI to explain its assumptions and not modify my project files.

### AI Response
The AI generated a class diagram containing Student, Task, TaskType, and Priority.

It also suggested relationships between Student and Task, Task and TaskType, and Task and Priority.

I saved the original response in `AI_DOMAIN_MODEL_DRAFT.md` before making my own changes.

### Changes I Made
1. Removed the Student class because the application does not currently require student accounts.
2. Removed the Student-to-Task relationship because it was based on an assumption.
3. Kept Task as the main class with the required task information.
4. Kept TaskType and Priority as enumerations.
5. Simplified the model by removing the isOverdue operation from the diagram.

### Reason for Changes
I wanted the final model to follow my IAP M2 requirements without adding unnecessary classes or relationships.

The application only needs to manage academic tasks at this stage.

### Verification
I compared the final diagram with my IAP M2 requirements and reviewed the differences between my model and the AI draft.

I created the final diagram using Mermaid and exported it as a PNG image.

The full critique is documented in `AI_MODEL_CRITIQUE.md`.
## IAP M4 — ADR-001

### AI Prompt
I asked ChatGPT to help me write an Architecture Decision Record for my Student Task Tracker. The decision was whether to keep or remove the Student class from my domain model. I asked for the context, decision, two alternatives, and positive and negative consequences.

### AI Response Summary
ChatGPT suggested removing the Student class because the current application does not require student accounts. It explained the advantages of a simpler domain model and the disadvantages of adding student accounts later.

### My Decision
I chose to remove the Student class and keep Task as the main class. This matches the decision I made during IAP M3.

### Changes and Review
I checked that the ADR explains why I made the decision, includes two alternatives, and describes what becomes harder because of my choice. I kept the decision consistent with my final domain model.

### Verification
I saved the decision in docs/adr/ADR-001.md. I will commit the ADR and this log to GitHub.
## IAP M5 — Walking Skeleton and CI Setup

### AI Prompt
I asked ChatGPT to help me build a basic working version of my Student Task Tracker using Django. I also asked for help setting up automated tests and GitHub Actions so I could check whether my project works correctly.

### AI Response Summary
ChatGPT helped me understand how to connect the Django model, views, URLs, and HTML template. It also explained how to create tests using pytest and configure a GitHub Actions workflow to run the tests automatically.

### My Changes and Decisions
I worked on the Django project and connected the Task model to the web page. I fixed a TemplateDoesNotExist error by checking the template folder and Django settings. I also tested the application by adding an assignment and checking that it was saved in the database.

I added automated tests and configured the CI workflow in `.github/workflows/ci.yml`.

### Verification
I ran `python -m pytest -v` in VS Code, and both tests passed.

I also pushed my project to GitHub and checked the GitHub Actions results. The workflow completed successfully, including the Django system checks, database migrations, and automated tests.

**GitHub Actions Evidence:**
https://github.com/obenggeorge-art/eece4081-iap-task-tracker/actions/runs/38678345949/job/116236966333#step:17:2

### What I Learned
I learned how the different parts of a Django application work together. I also learned how automated testing and continuous integration help detect problems when changes are made to a project.