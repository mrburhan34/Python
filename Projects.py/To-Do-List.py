tasks = []

def updateTask():
    upIndex = int(input("Enter the number which you want to update: "))
    if upIndex >= 0 and upIndex < len(tasks):
        up = input("Enter your updated task: ")
        tasks[upIndex] = up
    else:
        print("Invalid input!")

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to my first app")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Update task")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            updateTask()
        elif(choice == "4"):
            listTasks()
        elif(choice == "5"):
            break
        else:
            print("Invalid input!")