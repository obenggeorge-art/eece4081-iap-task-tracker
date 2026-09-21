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