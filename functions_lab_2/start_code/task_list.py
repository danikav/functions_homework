tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks
def find_uncompleted_tasks(task_list):
    uncompleted_tasks = []
    for task in task_list:
        if task["completed"] == False:
            uncompleted_tasks.append(task["description"])
    return uncompleted_tasks

tasks_remaining = find_uncompleted_tasks(tasks)
# print(tasks_remaining)

# 2. Print a list of completed tasks
def find_completed_tasks(task_list):
    completed_tasks = []
    for task in task_list:
        if task["completed"] == True:
            completed_tasks.append(task["description"])
    return completed_tasks

tasks_done = find_completed_tasks(tasks)
# print(tasks_done)

# 3. Print a list of all task descriptions
def find_task_description(task_list):
    all_tasks = []
    for task in task_list:
        all_tasks.append(task["description"])
    return all_tasks

tasks_description = find_task_description(tasks)
# print(tasks_description)

# 4. Print a list of tasks where time_taken is at least a given time
def find_time_taken_at_least(task_list, time):
    time_taken_at_least = []
    for task in task_list:
        if task["time_taken"] >= time:
            time_taken_at_least.append(task)
    return time_taken_at_least

tasks_that_take_at_least_15_minutes = find_time_taken_at_least(tasks, 15)
# print(tasks_that_take_at_least_15_minutes)

# 5. Print any task with a given description
def find_task_with_description(task_list, description_name):
    task_with_description = []
    for task in task_list:
        if task["description"] == description_name:
            task_with_description.append(task)
    return task_with_description

walk_dog_task = find_task_with_description(tasks, "Walk Dog")
# print(walk_dog_task)

# ### Extension

# 6. Given a description update that task to mark it as complete.
def update_description(task_list, description_name):
    for task in task_list:
        if task["description"] == description_name:
           task["completed"] = True
    return 

update_feed_cat_task = update_description(tasks, "Feed Cat")
# print(tasks)

# 7. Add a task to the list
def add_task(task_list, description, completed_status, time_taken):
    task_list.append({"description": description, "completed": completed_status, "time_taken": time_taken})
    return 

add_feed_dog_task = add_task(tasks, "Feed Dog", False, 5)
# print(tasks)

# ### Further Extensions

# 8. Use a while loop to display the following menu and allow the use to enter an option.

def display_menu(task_list):
    user_input = None
    while user_input == None:
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        user_input = input("Input")
        if user_input == "1":
            print(find_task_description(tasks))
        elif user_input == "2":
            print(find_uncompleted_tasks(tasks))
        elif user_input == "3":
            print(find_completed_tasks(tasks))
        elif user_input == "4":
            print(update_description(tasks, "Feed Cat"))
        elif user_input == "5":
            print(find_time_taken_at_least(tasks, 15))
        elif user_input == "6":
            print(find_task_with_description(tasks, "Walk Dog"))
        elif user_input == "7":
            print(add_task(tasks, "Feed Dog", False, 5))
        elif user_input == "M" or user_input == "m":
            print(display_menu(tasks))
        elif user_input == "Q" or user_input == "q":
            exit()
        

display_menu(tasks)

# 9. Call the appropriate function depending on the users choice.
