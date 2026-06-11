import json

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty!")
        return

    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== TASK LIST =====")

    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{i}. {task['task']} - {status}")

# Delete task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Mark task as completed
def mark_completed(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Main Program
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_completed(tasks)

    elif choice == "5":
        print("Thank you for using To-Do List Application!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")