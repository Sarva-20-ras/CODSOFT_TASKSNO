# TO-DO LIST APPLICATION

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks added yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter your task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()

    if len(tasks) > 0:
        number = int(input("\nEnter task number to delete: "))

        if number >= 1 and number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print(f"'{deleted}' deleted successfully!")
        else:
            print("Invalid task number.")

def mark_completed():
    show_tasks()

    if len(tasks) > 0:
        number = int(input("\nEnter task number completed: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1] = tasks[number - 1] + " - Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        mark_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")