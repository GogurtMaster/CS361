class Task ():
    def __init__(self, name, description, duedate, priority):
        self.name = name
        self.description = description
        self.duedate = duedate
        self.priority = priority

    def __str__(self):
        return f"Task Name: {self.name}, Due Date: {self.duedate}, Priority: {self.priority}"

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.name = description

    def set_duedate(self, duedate):
        self.duedate = duedate

    def set_priority(self, priority):
        self.priority = priority
    

def create_tasks(tasks):
    task_name = input("Enter the Name of the Task: \n")
    task_description = input("\nPlease Enter a Short Description of the Task: \n")
    task_duedate = input("\nPlease Enter the Due Date of the Task Using Month/Date/year Format: \n")
    task_priority = input("\nPlease Enter the Priority of the Task on a Scale of 1 - 10 With 1 being most important: \n")

    task = Task(task_name.lower(), task_description.lower(), task_duedate, task_priority)

    tasks.append(task)
    return

def menu(tasks, purpose):
    while (True):
        print("\nPlease Select an Option by Entering the Number Below:\n")
        print(f"1. {purpose} Task\n")
        print("2. Show all Tasks\n")
        print("3. Return to Main Menu\n")

        user = input()

        if user == "1":
            name = input(f"\nEnter the Name of the Task You Want to {purpose}: \n")
            return name

        elif user == "2":
            print_tasks(tasks)

        elif user == "3":
            return False


def delete_task(tasks):
    user = menu(tasks, "Delete")

    if user == False:
        return
    else:
        name = user
        delete = input(f"\n{name} will be perminatly deleted are you sure [yes/no]:\n")

    if delete.lower() == "yes":
        for i, item in enumerate(tasks):
            if item.name.lower() == name.lower():
                del tasks[i]
                print(f"\nDeleted {name}\n")
                break
        else:
            print(f"No Task Called {name} Was Found.")

    else:
        print(f"\n{name} Was Not Deleted\n")

    return tasks

def update_task(tasks):
    user = menu(tasks, "Update")

    if user == False:
        return
    else:
        task_name = user

    user_task = None
    for task in tasks:
        if task.name.lower() == task_name:
            user_task = task
            break
    else:
        print("That Task was not Found in the List")
        return

    user_change = input("\n\nWould You Like to Update the Name, Description, Due Date, or the Priority of the Task?:\n")
    
    if user_change.lower() == "name":
        new_name = input("\nPlease Enter the New Name of the Task:\n")
        user_task.set_name(new_name)

    elif user_change.lower() == "description":
        new_description = input("\nPlease Enter the New Description of the Task:\n")
        user_task.set_description(new_description)

    elif user_change.lower() == "duedate":
        new_duedate = input("\nPlease Enter the New Date of the Task Using Month/Date/year Format:\n")
        user_task.set_duedate(new_duedate)
    
    elif user_change.lower() == "due date":
        new_duedate = input("\nPlease Enter the New Date of the Task Using Month/Date/year Format:\n")
        user_task.set_duedate(new_duedate)

    elif user_change.lower() == "priority":
        new_priority = input("\nPlease Enter the New Priority of the Task on a Scale of 1 - 10 With 1 being most important:\n")
        user_task.set_priority(new_priority)

def print_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo Task Right Now!!\n\n")

    else:
        for i in tasks:
                print(f"\n{i}")


# def find_task(tasks, user_task):
#     for i in tasks:
#         if i == user_task:
#             return i


tasks = []

print("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                      
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                     
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                     
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                     
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝   
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝   
      
████████╗ █████╗ ███████╗██╗  ██╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
   ██║   ███████║███████╗█████╔╝     ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
   ██║   ██╔══██║╚════██║██╔═██╗     ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████║██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")

# used "https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=task%20manager" to generate ascii text, Font name: ANSI shadow

print("\n\nTo Get Started Please Enter 1 to Create a Task!\n")

while(True):
    print("\nPlease Select an Option by Entering the Number Below:\n")
    print("1. Add Task: create a new task and add it to the list of tasks\n")
    print("2. Remove Task: Remove an existing task from them list (this will perminatly delete the task)\n")
    print("3. Update Task: change the name, description, due date, or priority of a task\n")
    print("4. Show Tasks: display all tasks")

    user = input()
    if user == "1":
        create_tasks(tasks)

    elif user == "2":
        delete_task(tasks)

    elif user == "3":
        update_task(tasks)

    elif user == "4":
        print_tasks(tasks)
    
    elif user == "5":
        task = Task("task 1", "this is the first task in the list", "12/30/2024", "2")
        tasks.append(task)
        task = Task("task 2", "this is the second task in the list", "1/28/2026", "9")
        tasks.append(task)
        task = Task("task 3", "this is the third task in the list", "11/30/2024", "1")
        tasks.append(task)
        task = Task("task 4", "this is the fourth task in the list", "6/17/2025", "7")
        tasks.append(task)
        task = Task("task 5", "this is the fifth task in the list", "2/28/2025", "4")
        tasks.append(task)


