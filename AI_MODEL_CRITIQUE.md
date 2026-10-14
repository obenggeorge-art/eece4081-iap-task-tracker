# AI Domain Model Critique

## IAP M3 — Domain Model and AI Critique

### 1. Introduction

For this assignment, I used GitHub Copilot to generate the first domain model for my Student Task Tracker application. I then reviewed the AI model and compared it with the requirements I wrote in IAP M2.

My goal was to create a simple model that supports the application without adding unnecessary classes or relationships.

### 2. Over-Modeling

The AI included a Student class with a studentId and connected it to the Task class.

I decided to remove the Student class because my current application does not require students to create accounts or log in. The application is designed to track tasks, and the requirements do not specify a multi-user system.

Adding the Student class would introduce an extra relationship that the current requirements do not need.

### 3. Under-Modeling

The AI model included the main task information, but it did not clearly show which fields could be optional.

For example, the model did not indicate whether a task could exist without a due date or priority. This is important because the application should handle tasks that do not have all their details available.

The model also did not clearly explain how the application would display overdue tasks. Although the AI included an isOverdue operation, I chose to keep the final model focused on the main task attributes. Overdue status can be calculated using the due date and completion status.

### 4. Guessed Relationships

The AI assumed that each task belongs to exactly one student and that one student can have many tasks.

This relationship would make sense for an application with multiple student accounts. However, my IAP M2 requirements do not mention accounts, authentication, or managing multiple students.

I removed this relationship because it was based on an assumption rather than a requirement.

### 5. What the AI Got Right

The AI correctly identified Task as the main class.

It also included important attributes such as taskId, title, type, dueDate, priority, and isCompleted. These support the requirements for creating, editing, viewing, and completing tasks.

The AI also correctly suggested TaskType and Priority as enumerations instead of separate database entities.

The TaskType enumeration includes Assignment, Exam, Project, and Other. The Priority enumeration includes Low, Medium, and High.

These choices make the model easier to understand and help keep the task information consistent.

### 6. My Final Decision

My final domain model contains one main class, Task, and two enumerations, TaskType and Priority.

I removed the Student class because it is not needed for the current application. I also kept pending and completed tasks in the same Task class, using isCompleted to distinguish them.

This design supports my IAP M2 requirements while keeping the model simple and avoiding unnecessary relationships.

### 7. Conclusion

Using AI helped me identify the main parts of my application, but I learned that AI-generated models should not be accepted without reviewing them.

The AI made some useful suggestions, but it also introduced assumptions that were not supported by my requirements.

By comparing the AI draft with my own model, I was able to make a simpler design that better matches what I plan to build.