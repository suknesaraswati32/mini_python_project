def add_task(tasks, title, priority, due):
    tasks.append({
        "title": title,
        "priority": priority,
        "due": due,
        "completed": False
    })


def view_tasks(tasks):
    for task in tasks:
        print(task)


def delete_task(tasks, title):
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print("Task deleted")
            return


def complete_task(tasks, title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            print("Task completed")