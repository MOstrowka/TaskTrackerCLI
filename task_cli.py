#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime

# Define the path for the tasks JSON file
TASKS_FILE = 'tasks.json'


# Function to initialize the tasks JSON file if it doesn't exist
def initialize_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            json.dump([], file)  # Start with an empty list of tasks


# Function to load tasks from the JSON file
def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)


# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


# Function to add a new task
def add_task(description):
    tasks = load_tasks()  # Load existing tasks
    new_id = max([task['id'] for task in tasks], default=0) + 1  # Find the next available ID
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)  # Add the new task to the list
    save_tasks(tasks)  # Save the updated list to the JSON file
    print(f"Task added successfully (ID: {new_id})")


# Function to update an existing task
def update_task(task_id, description):
    tasks = load_tasks()  # Load existing tasks
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)  # Save the updated list to the JSON file
            print(f"Task ID {task_id} updated successfully.")
            return
    print(f"No task found with ID {task_id}.")


# Function to delete a task
def delete_task(task_id):
    tasks = load_tasks()  # Load existing tasks
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) < len(tasks):  # If a task was removed
        save_tasks(updated_tasks)  # Save the updated list to the JSON file
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"No task found with ID {task_id}.")


# Function to list tasks, optionally filtered by status
def list_tasks(status):
    tasks = load_tasks()  # Load existing tasks
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print(f"No tasks found with status '{status}'" if status else "No tasks found.")
    else:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, "
                  f"Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")


# Function to mark a task as in progress
def mark_task_in_progress(task_id):
    tasks = load_tasks()  # Load existing tasks
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "in-progress"
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)  # Save the updated list to the JSON file
            print(f"Task ID {task_id} marked as in-progress.")
            return
    print(f"No task found with ID {task_id}.")


# Function to mark a task as done
def mark_task_done(task_id):
    tasks = load_tasks()  # Load existing tasks
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "done"
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)  # Save the updated list to the JSON file
            print(f"Task ID {task_id} marked as done.")
            return
    print(f"No task found with ID {task_id}.")


# Function to display help information
def show_help():
    help_text = """
Task Tracker CLI - Available Commands:

1. Add a new task:
   task-cli add "Task description"
   Example: task-cli add "Buy groceries"

2. Update an existing task:
   task-cli update <id> "New description"
   Example: task-cli update 1 "Buy groceries and cook dinner"

3. Delete a task:
   task-cli delete <id>
   Example: task-cli delete 1

4. Mark a task as in progress:
   task-cli mark-in-progress <id>
   Example: task-cli mark-in-progress 1

5. Mark a task as done:
   task-cli mark-done <id>
   Example: task-cli mark-done 1

6. List all tasks:
   task-cli list

7. List tasks by status:
   task-cli list <status>
   Available statuses: todo, in-progress, done
   Examples: 
   task-cli list todo
   task-cli list done
   task-cli list in-progress

8. Display help:
   task-cli help
   """
    print(help_text)


# Main function to handle CLI commands
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    # Subparsers for different commands
    subparsers = parser.add_subparsers(dest='command')

    # Command to add a new task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # Command to update an existing task
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description of the task')

    # Command to delete a task
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    # Command to list all tasks
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'],
                             help='Filter tasks by status')

    # Command to mark a task as in progress
    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in progress')
    in_progress_parser.add_argument('id', type=int, help='ID of the task to mark as in progress')

    # Command to mark a task as done
    done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    done_parser.add_argument('id', type=int, help='ID of the task to mark as done')

    # Command to display help
    help_parser = subparsers.add_parser('help', help='Display help information')

    args = parser.parse_args()

    # Handle each command based on input
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'mark-in-progress':
        mark_task_in_progress(args.id)
    elif args.command == 'mark-done':
        mark_task_done(args.id)
    elif args.command == 'help':
        show_help()
    else:
        parser.print_help()


# Entry point for the script
if __name__ == '__main__':
    initialize_tasks_file()
    main()
