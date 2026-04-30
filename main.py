from task_manager import add_task, view_tasks, delete_task, complete_task
from storage import load_tasks, save_tasks

tasks = load_tasks()

while True:
    print("\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Mark Complete\n5.Save & Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Task name: ")
        priority = input("Priority (High/Medium/Low): ")
        due = input("Due date: ")
        add_task(tasks, title, priority, due)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        title = input("Task to delete: ")
        delete_task(tasks, title)

    elif choice == "4":
        title = input("Task completed: ")
        complete_task(tasks, title)

    elif choice == "5":
        save_tasks(tasks)
        break