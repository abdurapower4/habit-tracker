from tasks import Tasks
from datetime import datetime

def existing_tasks():
    tasks = Tasks.get_tasks();
    
    for task in tasks:
        print(f"Task Id: {task[0]}", f"Task: {task[1]}", f"Status: {task[2]}",f"Created: {task[5]}",f"Completed: {task[6]}")
print("###################################")
date = datetime.now();
day = date.strftime('%A')
print("<<<<<<<<<<<<<<<<< ***** >>>>>>>>>>>>")
print("                  Today is "+day)
print("<<<<<<<<<<<<<<<<< ***** >>>>>>>>>>>>")
print("************ <<<<<>>>>> ************ \n")
existing_tasks()
print("------------------****************-------------------------****************----------------**************------------")
print("\n ###################################")

def create_tasks():
    task = Tasks()
    tasks = input("Enter Task Name:- \n")
    days = input("Enter Days :- \nn(1). Monday,\n2). Tuesday,\n3). Wednesday,\n4). Thursday,\n5). Friday,\n6). Saturday,\n7). Sunday,\n8). Weekly): \nn")
    day = "Monday"

    if days == "1":
        day = "Monday"
    elif days == "2":
        day = "Tuesday"
    elif days == "3":
        day = "Wednesday"
    elif days == "4":
        day = "Thursday"
    elif days == "5":
        day = "Friday"
    elif days == "6":
        day = "Saturday"
    elif days == "7":
        day = "Sunday"
    elif days == "8":
        day = "Weekly"
    else:
        print("Oops! your selection is out of range")
        create_tasks()
    task.create_task(tasks,days.capitalize())
    
def fetch_all_task():
    task = Tasks.get_tasks()

fetch_all_task()

def complete_task(id):
    task = Tasks.complete_task(id)
    
def delete_task(id):
    task = Tasks.delete_tasks(id)

def single_task(id):
    task = Tasks.get_task(id)
    return task

def update_schedule(day,id,status):
    task = Tasks.set_dateCompleted(day,id,status)
    
def weekly_habits():
    tasks = Tasks.all_daily_habits()
    if len(tasks) > 0:
        for task in tasks:
            print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")
    else:
        print("You currently have no daily habits.")
        
def longest_streaks():
    tasks = Tasks.longest_streak()
    return tasks
    
def least_streaks():
    tasks = Tasks.least_streak()
    return tasks

def struggle_week():
    tasks = Tasks.least_streak()
    print(tasks)
    
def brocken_tasks():
    tasks = Tasks.brocken_habits("No")
    for task in tasks:
        print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")    

print("###################################")
print("Please select an action number.")
print("1). Add Task.")
print("2). Mark Task as Completed")
print("3). Delete Task")
print("4). Which habits did i break")
print("5). what’s my longest habit streak?")
print("6). What's the list of my current daily habits?")
print("7). which habits did I struggle most last month?")
print("###################################")
action = input("Input Selection:  \n ")

def recusive_function():
    print("###################################")
    print("Please select an action number.")
    print("1). Add Task.")
    print("2). Mark Task as Completed")
    print("3). Delete Task")
    print("4). Which habits did i break")
    print("5). what’s my longest habit streak?")
    print("6). What's the list of my current daily habits?")
    print("7). which habits did I struggle most last month?")
    print("################################### \n")
    action = input("Input Selection:  \n ")
    if action == "1":
        create_tasks()
        existing_tasks()
    elif action == "2":
        existing_tasks()
        task_id = input("Please Enter the ID of the task")
        complete_task(task_id)
        task_d = single_task(task_id)
        print(task_d[3])
        date = datetime.now()
        day = date.strftime('%A')
        update_schedule(day.capitalize(),task_id,"Checked-Off")
        if task_d[3] != "Weekly":
            if task_d[3] != day :
                Tasks.not_ontrack(task_id)
                print("you broke the habit")
        existing_tasks()
    elif action == "3":
        task_id = input("Please Enter the ID of the task")
        if task_id.isdigit():
            delete_task(task_id)
            existing_tasks()
        else:
            print("Oops! doesn't seem like you picked a number")
    elif action == "4":
        print("*************************************")
        print("*************   Habits i break  ******")
        print("*************************************\n")
        brocken_tasks()
    elif action == "5":
        print("*************************************")
        print("Longest habit streak")
        print("*************************************\n")
        longest = longest_streaks()
        task = single_task(longest[0][0])
        print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")
    elif action == "6":
        print("*************************************")
        print("Current daily habits")
        print("*************************************\n")
        weekly_habits()
    elif action == "7":
        print("*************************************")
        print("Most struggled habits")
        print("*************************************\n")
        least = least_streaks()
        task = single_task(least[0][0])
        print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")
    else:
        print("You made an invalid selection.")
        print("###################################\n")
        print("Please select an action number.")
        print("1). Add Task.")
        print("2). Mark Task as Completed")
        print("3). Delete Task")
        print("4). Which habits did i break")
        print("5). what’s my longest habit streak?")
        print("6). What's the list of my current daily habits?")
        print("7). which habits did I struggle most last month?")
        print("###################################\n")
        action = input("Input Selection:  \n ")
        existing_tasks()




if action == "1":
    create_tasks()
    existing_tasks()
    recusive_function()
elif action == "2":
    existing_tasks()
    task_id = input("Please Enter the ID of the task")
    complete_task(task_id)
    task_d = single_task(task_id)
    print(task_d[3])
    date = datetime.now()
    day = date.strftime('%A')
    update_schedule(day.capitalize(),task_id,"Checked-Off")
    if task_d[3] != "Weekly":
        if task_d[3] != day :
            Tasks.not_ontrack(task_id)
            print("you broke the habit")
    existing_tasks()
    print("*************************************")
    recusive_function()
elif action == "3":
    task_id = input("Please Enter the ID of the task")
    if task_id.isdigit():
        delete_task(task_id)
        existing_tasks()
        print("*************************************")
        recusive_function()
    else:
        print("Oops! doesn't seem like you picked a number")
        print("*************************************")
        recusive_function()
elif action == "4":
    print("*************************************")
    print("Habits i break")
    print("*************************************")
    brocken_tasks()
    print("*************************************")
    recusive_function()
elif action == "5":
    print("*************************************")
    print("Longest habit streak")
    print("*************************************")
    longest = longest_streaks()
    task = single_task(longest[0][0])
    print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")
    print("*************************************")
    recusive_function()
elif action == "6":
    print("*************************************")
    print("Current daily habits")
    print("*************************************")
    weekly_habits()
    print("*************************************")
    recusive_function()
elif action == "7":
    print("*************************************")
    print("Most struggled habits")
    print("*************************************")
    least = least_streaks()
    task = single_task(least[0][0])
    print(f"Task Id: {task[0]}", "Task: {task[1]}", "Status: {task[2]}")
    print("*************************************")
    recusive_function()
else:
    print("You made an invalid selection.")
    recusive_function()

