
# Task Tracker CLI

Task Tracker CLI is a simple command-line interface (CLI) application for tracking and managing your tasks. This project is designed to help you keep track of what you need to do, what you have done, and what you are currently working on.

## Features

- **Add tasks:** Create a new task with a unique ID.
- **Update tasks:** Modify the description of an existing task.
- **Delete tasks:** Remove a task using its ID.
- **Mark tasks as in-progress or done:** Update the status of tasks to reflect their current state.
- **List tasks:** View all tasks or filter tasks by their status (e.g., `todo`, `in-progress`, `done`).

## Installation

1. **Clone the repository:**

   ```bash
   git clone <URL_OF_YOUR_REPOSITORY>
   cd TaskTrackerCLI
   ```

2. **Ensure Python (3.x) is installed and accessible via the command line.**

## Usage

To use the Task Tracker CLI application, open a terminal, navigate to the project directory, and use the following commands:

### Adding a New Task

```bash
task-cli add "Task description"
```

**Example:**

```bash
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a Task

```bash
task-cli update <id> "New task description"
```

**Example:**

```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Deleting a Task

```bash
task-cli delete <id>
```

**Example:**

```bash
task-cli delete 1
```

### Marking a Task as In Progress

```bash
task-cli mark-in-progress <id>
```

**Example:**

```bash
task-cli mark-in-progress 1
```

### Marking a Task as Done

```bash
task-cli mark-done <id>
```

**Example:**

```bash
task-cli mark-done 1
```

### Listing All Tasks

```bash
task-cli list
```

### Listing Tasks by Status

```bash
task-cli list <status>
```

**Available statuses:** `todo`, `in-progress`, `done`

**Examples:**

```bash
task-cli list todo
task-cli list done
task-cli list in-progress
```

### Displaying Help

```bash
task-cli help
```

## Task Properties

Each task has the following properties:
- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

These properties are stored in a JSON file (`tasks.json`) and are updated whenever tasks are added, modified, or deleted.

## Project URL

For more details about this project, visit the [Task Tracker Project Page](https://roadmap.sh/projects/task-tracker).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
