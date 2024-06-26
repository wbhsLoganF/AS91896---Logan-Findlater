import easygui

"""Setting out the nested dictionary, which houses all tasks"""
tasks = {
    1:{
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "In Progress",
    },
    2:{
        "Title": "Implement Login Page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "Blocked",
    },
    3:{
        "Title": "Fix Navigation Menu",
        "Description": "Fix the navigation menu to be more user friendly",
        "Assignee": "None",
        "Priority": 1,
        "Status": "Not Started",
    },
    4:{
        "Title": "Add Payment Processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": 2,
        "Status": "In Progress",
    },
    5:{
        "Title": "Create an About Us Page",
        "Description": "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": 1,
        "Status": "Blocked",
    }
}

"""Setting out another nested dictionary, which details all members of 
the company"""
members = {
    "JSM":{
        "Name": "John Smith",
        "Email": "John@techvision.com",
        "Tasks Assigned": ""
    },
    "JLO":{
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks Assigned": ""
    },
    "BDI":{
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Tasks Assigned": ""
    }
}


"""Establishing variables and lists which are called for later on in 
the code"""

member_codes = []
for codes in members: 
    member_codes.append(codes)
member_codes.append("None")
status_choices = ["Not Started", "Blocked", "In Progress","Completed"]
update_choices = ["Assignee","Priority","Status"]
y_or_n= ["Yes","No"]
task_id= 1
blank = ""
aspect = ""
valid = False
big_space = "                                   "
space = "                        "
gap = "              "



def print_whole():
    """Displays entire nested dictionary in one msgbox by adding each
    element to an formatted output"""

    output = ""
    for item, item_info in tasks.items():
        output += (f"\nTask Number: {item} \n\n")  
        for key in item_info:
            output += (f"{key}: {item_info[key]}  \n")
    title = "LIST"
    easygui.msgbox(output, title)



def add_task():
    """Allows the user to add a new task to the database"""

    #Getting all information for the new task from the user.
    while valid == False:
        msg = "Enter a title for the task"
        title = easygui.enterbox(msg)
        if title == None or title == "":
            msg = f"{space}   A title is required"
            easygui.msgbox(msg)
        else:
            break
    
    #No validation check here as a description is not required.
    msg = "Enter a description of the task:"
    description = easygui.enterbox(msg)

    msg = f"{gap}Select a team member to assign to the task:"
    assignee = easygui.buttonbox(msg,blank,member_codes)

    while valid == False:
        msg ="Enter the priority of the task (1-3):"
        priority = easygui.integerbox(msg,lowerbound=1,upperbound=3)
        if priority == None or priority == "":
            msg = f"{space}A priority rating is required"
            easygui.msgbox(msg)
        else:
            break
    while valid == False:
        msg = f"{space}Enter the status of the task:"
        status = easygui.buttonbox(msg,blank,status_choices)
        if status == None or status == "":
            msg = f"{space}   A status is required"
            easygui.msgbox(msg)
        else:
            break

    #Finding the task id number to assign to the new task (sequential).
    task_number = 1
    for i in tasks:
        task_number += 1

    msg = f"So you want to add '{title}' to the task list?"
    confirm = easygui.buttonbox(msg,blank,y_or_n)

    #Adds the new entry to the tasks dictionary.
    if confirm == "Yes":
        tasks[task_number] = {
        "Title": title,
        "Description": description,
        "Assignee": assignee,
        "Priority": priority,
        "Status": status,
        }
        msg = f"{gap}{title} has been added to the database."
        title = "ENTRY ADDED"
        easygui.msgbox(msg, title)

    else:
        msg = f"{space}          Cancelled."
        easygui.msgbox(msg)



def assignee_search():
    """Allows the user to select a team member and see all non 
    completed tasks assigned to them"""

    #User selects a code from a list defined at the top.
    while valid == False:
        msg = f"{space}    Select a team member:"
        assignee = easygui.buttonbox(msg,blank,member_codes)
        if assignee == None or assignee == "":
            msg = "You must select a team member"
            easygui.msgbox(msg)
        else:
            break
    task_id = 1
    output = ""
    temp_dict = {}

    #Main chunk of code that runs through the tasks dictionary. If the 
    # assignee information matches the information in the assignee key 
    # of the dictionary, and the task is not marked as completed, it is
    # added to a new dictionary.
    for i in tasks:
        if assignee in tasks[task_id]["Assignee"] \
        and tasks[task_id]["Status"] != "Completed":
            temp_dict[task_id]={
                "Title": tasks[task_id]["Title"],
                "Description": tasks[task_id]["Description"],
                "Assignee": tasks[task_id]["Assignee"],
                "Priority": tasks[task_id]["Priority"],
                "Status": tasks[task_id]["Status"],
            }
        task_id += 1

    #Adding each aspect from every task in the new dictionary one by 
    # one to display aesthetically.
    for item, item_info in temp_dict.items():
        output += (f"\nTask Number: {item} \n\n")  
        for key in item_info:
            output += (f"{key}: {item_info[key]}  \n")

    title = f"TASKS ASSIGNED : {assignee}"
    easygui.msgbox(output, title)



def title_search():
    """Allows the user to select the title of a task from the 
    dictionary to recieve all information on it"""
    #Simple loop to simultaneously determine the amount of tasks in the 
    # database and pull the titles of the tasks into a list to display 
    # in a buttonbox, rather than displaying the task ids (as the user 
    # could have used the add_task function to add more than the base 
    # amount of 5).
    choices = []
    task_numbers = 1
    output = ""
    for i in tasks:
        choices.append(tasks[task_numbers]["Title"])
        task_numbers += 1

    #The user selects a title from the previously created list.
    msg = f"{space}Which task are you searching for?"
    title = "SELECT TASK"
    task = easygui.buttonbox(msg,title,choices)

    #Finding the task number (task_id) that the title selected goes 
    # with in order to display it individually.
    task_id = 1
    for i in tasks:
        if task in tasks[task_id]["Title"]:
            break
        else:
            task_id += 1

    temp_dict = {}
    temp_dict[task_id]={
                "Title": tasks[task_id]["Title"],
                "Description": tasks[task_id]["Description"],
                "Assignee": tasks[task_id]["Assignee"],
                "Priority": tasks[task_id]["Priority"],
                "Status": tasks[task_id]["Status"],
            }

    for item, item_info in temp_dict.items():
        output += (f"\nTask Number: {item} \n\n")  
        for key in item_info:
            output += (f"{key}: {item_info[key]}  \n")

    title = "TASK"
    easygui.msgbox(output, title)



def update():
    """Allows the user to change a task in the database, assignee, 
    priority, or status"""

    #Simple loop to simultaneously determine the amount of tasks in the 
    # database and pull the titles of the tasks into a list to display 
    # in a buttonbox, rather than displaying the task ids, which the 
    # user may not know.
    choices = []
    task_numbers = 1
    for i in tasks:
        choices.append(tasks[task_numbers]["Title"])
        task_numbers += 1

    #The user selects a title from the previously created list.
    msg = f"{space}Which task do you want to update?"
    title = "SELECT TASK"
    task = easygui.buttonbox(msg,title,choices)
    if task != None:
        #Finding the task number (task_id) that the title selected goes 
        # with in order to change another aspect of the task.
        task_id = 1
        for i in tasks:
            if task in tasks[task_id]["Title"]:
                break
            else:
                task_id += 1

        #User selects the aspect they would like to update from a list 
        # defined at the top, "Assignee, Priority, Status".
        while valid == False:
            msg = f"{gap}  What aspect of the task do you want to change?"
            title = "SELECT ASPECT"
            aspect = easygui.buttonbox(msg,title,update_choices)
            if aspect == None or aspect == "":
                msg = f"{gap}      You must select an aspect to change"
                easygui.msgbox(msg)
            else:
                break

        #Determining the users selected aspect to update, and getting 
        # the users input for the new value to be associated with it.
        while valid == False:
            if aspect == "Assignee":
                msg = f"{gap}     Who do you want the new assignee to be?"
                new = easygui.buttonbox(msg,blank,member_codes)

            elif aspect == "Priority":
                msg = "What do you want the new priority to be? (/3)"
                title = "ENTER PRIORITY"
                new = easygui.integerbox(msg,title,lowerbound=1,upperbound=3)

            elif aspect == "Status":
                msg = f"{gap}       What do you want the new status to be?"
                title = "SELECT STATUS"
                new = easygui.buttonbox(msg,title,status_choices)

            #Checking validation to make sure user hasn't clicking the 
            # close or exit "X" when the buttonboxes appear.
            if new == None or new == "":
                msg = f"{space}   A new value is required"
                easygui.msgbox(msg)
            else:
                break

        #Confirming the change to avoid user mistakes.
        msg = f"  So you want to change the {aspect} of '{task}' to '{new}'?"
        title = "CONFIRM"
        confirm = easygui.buttonbox(msg,title,y_or_n)

        #Using all gathered information to assign a 
        # new value to the selected task.
        if confirm == "Yes":
            tasks[task_id][aspect] = new
            msg = f"{big_space}  Done!"
            easygui.msgbox(msg)
        else:
            msg = f"{space}           Cancelled."
            easygui.msgbox(msg)



def report():
    """Generates a report of the projects progress, displaying the 
    number of tasks completed, in progress, blocked, and not started"""

    #Setting/resetting variables
    total = 0
    completed = 0
    in_progress = 0
    blocked = 0
    not_started = 0
    output = ""

    #Running through every task in the dictionary and checking its 
    # status. It then adds 1 point to whichever status it has.
    for task_id in tasks:
        total += 1
        if tasks[task_id]["Status"] == "Completed":
            completed += 1
        if tasks[task_id]["Status"] == "In Progress":
            in_progress += 1
        if tasks[task_id]["Status"] == "Blocked":
            blocked += 1
        if tasks[task_id]["Status"] == "Not Started":
            not_started += 1

    #Adding the numbers associated with each status option to an 
    # outputted message, so they will all be displayed in a single 
    # msgbox.
    output += f"Total Tasks: {total}\n\n"
    output += f"Tasks Completed: {completed}\n\n" 
    output += f"Tasks In Progress: {in_progress}\n\n"
    output += f"Tasks Blocked: {blocked}\n\n"
    output += f"Tasks Not Started: {not_started}"

    title = "REPORT"
    easygui.msgbox(output,title)




#Main menu with all options available as a buttonbox, which link to 
# their respective function.
while True:
    msg = f"{space}   Please choose an option:"
    title = "MAIN MENU"
    choices = ["Print whole","Search","Add a task","Update tasks",
    "Generate report","Quit"]
    main_menu = easygui.buttonbox(msg,title,choices)

    #Checking which function to run based off input from the main menu.
    if main_menu == "Print whole":
        print_whole()

    elif main_menu == "Search":
        msg = f"{space}How would you like to search?"
        title = "SEARCH"
        choices = ["Search by assignee","Search by title"]
        search_option = easygui.buttonbox(msg,title,choices)

        if search_option == "Search by assignee":
            assignee_search()
        elif search_option == "Search by title":
            title_search()

    elif main_menu == "Add a task":
        add_task() 

    elif main_menu == "Update tasks":
        update()

    elif main_menu == "Generate report":
        report()
    else:
        break

msg = "Goodbye!"
easygui.msgbox(f"{big_space} {msg}")