# Simple To-Do List Manager

def show_menu():
    print("\n✨ To-Do List Menu ✨")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save & Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet! ✅")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully! 🎉")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num-1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid choice ❌")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved. Goodbye! 👋")

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid option, try again!")
