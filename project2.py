task = input("Enter the task: ")
li = []

def add_task(task):
  li.append(task)
  print("task added successfully")

def del_task(task):
    if task in li:
        li.remove(task)
        print("task deleted successfully")
    else:
        print("task not found")

def completed_task(task):
    if task in li:
        li.remove(task)
        print(f"{task} is completed")
    else:
        print("task not found")

def save(file_name, task):
    with open(file_name, "w") as f:
        f.write(task)
        print("task is saved")

while True:
    print("\n1.Add Task")
    print("2.Delete Task")
    print("3.Complete Task")
    print("4.Save Task")
    print("5.Show Tasks")
    print("6.Exit")

    case = int(input("Enter a case: "))

    match case:
        case 1:
            add_task(task)

        case 2:
            del_task(task)

        case 3:
            completed_task(task)

        case 4:
            save("ask.txt", task)

        case 5:
            print(li)

        case 6:
            break

        case _:
            print("invalid case")