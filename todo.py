# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to mark a task as done
def mark_done():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            done_task = tasks.pop(task_num - 1)
            print(f"Task '{done_task}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")

# End of the program
print("Goodbye!")
