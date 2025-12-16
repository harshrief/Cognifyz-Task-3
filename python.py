class Task:
    def __init__(self, task_id, title, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id} | Task: {self.title} | Status: {self.status}"


tasks = []
task_counter = 1

def create_task():
    global task_counter
    title = input("Enter task title: ")
    task = Task(task_counter, title)
    tasks.append(task)
    print("Task added successfully!")
    task_counter += 1

def read_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for task in tasks:
            print(task)

def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            new_title = input("Enter new title: ")
            new_status = input("Enter status (Pending/Completed): ")
            task.title = new_title
            task.status = new_status
            print("Task updated successfully!")
            return
    print("Task not found!")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found!")


while True:
    print("\n=== TASK MANAGER ===")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice! Try again.")
