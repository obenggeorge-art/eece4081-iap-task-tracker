
# EECE 4081 Individual Application Project

## Student Task Tracker

**Student:** George Kakra Obeng  
**Course:** EECE 4081 — Software Engineering  
**University:** University of Memphis

## 1. Project Overview

The Student Task Tracker is a web application designed to help students organize their academic work. Students can create tasks for assignments, exams, projects, and other school responsibilities.

The application was developed as an Individual Application Project to practice software engineering concepts, including requirements engineering, domain modeling, design decisions, testing, refactoring, logging, and dependency management.

## 2. Implemented Features

- Create an academic task.
- Enter a task title and due date.
- Select a task type: Assignment, Exam, Project, or Other.
- Select a priority: Low, Medium, or High.
- Save tasks to a SQLite database.
- Display saved tasks in due-date order.
- Record task creation events using structured JSON logging.

The Task model also contains a completion-status field. A user-facing feature for marking tasks as completed remains future work.

## 3. Technology Stack

- Python 3.12
- Django
- SQLite
- pytest and pytest-django
- Git and GitHub
- GitHub Actions
- Visual Studio Code

Dependency versions are recorded in `requirements.txt`.

## 4. Installation and Setup

Clone the repository:

```bash
git clone https://github.com/obenggeorge-art/eece4081-iap-task-tracker.git
cd eece4081-iap-task-tracker
```

Create and activate a virtual environment.

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Apply database migrations:

```powershell
python manage.py migrate
```

Start the application:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

## 5. Testing

Run the automated test suite:

```powershell
python -m pytest -v
```

During M9 verification on November 17, 2026, all six tests passed.

The tests cover task creation and viewing, due-date ordering, default completion status, priority choices, task types, and string representation.

## 6. Project Milestones

| Milestone | Work Completed |
|---|---|
| M1 | Repository initialization and toolchain setup |
| M2 | User stories, non-functional requirements, and AI elicitation audit |
| M3 | Domain model and AI-generated model critique |
| M4 | Architecture Decision Record ADR-001 |
| M5 | Working task creation and listing workflow |
| M6 | Automated tests and bug-injection demonstration |
| M7 | Refactoring with regression testing |
| M8 | Structured JSON logging and troubleshooting runbook |
| M9 | Dependency and license audit with compatibility-risk analysis |

## 7. Dependency and License Audit

M9 reviewed the project's declared and installed Python dependencies.

Verification included:

- Python 3.12.10
- Dependency installation
- `pip check` with no broken requirements
- Six passing automated tests
- License metadata collected using pip-licenses

The license report identified permissive licenses, including MIT, BSD, and Apache-2.0.

No obvious copyleft conflict was identified among the reported packages.

The main compatibility risk is that future Python, Django, or dependency upgrades may introduce incompatibilities. Pinned dependencies and automated testing help reduce this risk.

See:

- `IAP_M9_DEPENDENCY_LICENSE_AUDIT.md`
- `M9_LICENSE_REPORT.md`
- `M9_INSTALLED_PACKAGES.txt`

## 8. Documentation

The repository contains requirements, domain-model documentation, design decisions, testing evidence, refactoring notes, structured logging examples, and the M8 troubleshooting runbook.

The `PROMPT_DIFF_LOG.md` file records AI assistance and development changes across milestones.

## 9. Future Improvements

Potential improvements include:

- Marking tasks as completed through the interface.
- Editing and deleting tasks.
- Filtering tasks by priority or type.
- Adding deadline reminders.
- Improving form validation and user feedback.

These are proposed improvements, not claims about the current implementation.

## 10. Conclusion

This project helped me understand how software engineering practices support the development of a working application. I gained experience in planning requirements, making design decisions, implementing features, writing tests, improving code, and documenting technical work.

The result is a small database-backed task tracker with a tested task-creation workflow.
