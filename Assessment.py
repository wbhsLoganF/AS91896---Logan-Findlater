import easygui

"""Setting out the nested dictionary, which houses all tasks"""
tasks = {
    "1":{
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "In Progress",
    },
    "2":{
        "Title": "Implement Login Page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "Blocked",
    },
    "3":{
        "Title": "Fix Navigation Menu",
        "Description": "Fix the navigation menu to be more user friendly",
        "Assignee": "None",
        "Priority": 1,
        "Status": "Not Started",
    },
    "4":{
        "Title": "Add Payment Processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": 2,
        "Status": "In Progress",
    },
    "5":{
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


"""Establishing variables which are called for later on in the code"""
member_codes = []
for codes in members: 
    member_codes.append(codes)
member_codes.append("None")



"""All functions will now be added"""

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

    #Getting all information for the new task from the user
    msg = "Enter a title for the task"
    title = easygui.enterbox(msg)
    msg = "Enter a description of the task:"
    description = easygui.enterbox(msg)
    msg = "Select a team member to assign to the task:"
    blank = ""
    choices = member_codes
    assignee = easygui.buttonbox(msg,blank,choices)
    msg ="Enter the priority of the task (1-3):"
    priority = easygui.integerbox(msg)
    msg = "Enter the status of the task:"
    status = easygui.enterbox(msg)

    #Add the new entry to the tasks dictionary
    task_number = 1
    for i in tasks:
        task_number += 1
        
    tasks[task_number] = {
        "Title": title,
        "Description": description,
        "Assignee": assignee,
        "Priority": priority,
        "Status": status,
    }
    msg = f"{title} has been added to the database."
    title ="Entry Added"
    easygui.msgbox(msg, title)


def delete_task():
    """Allows the user to remove a task from the dictionary entirely
    """

    categories = [] 
    title = "SELECT" 
    msg = "Click on the task you would like to remove" 
    #Adding the tasks from the dictionary to a list
    for task in tasks: 
        categories.append(task) 

    #Getting the users choice
    deleted_task = easygui.buttonbox(msg, title, categories) 
    msg= f"Are you sure you want to delete {deleted_task}?"
    title = "CONFIRM"
    choices = ["Yes","No"]
    confirm = easygui.buttonbox(msg,title,choices)

    #Confirming the choice
    if confirm == "Yes":
        del tasks[delete_task]
        msg = "Done!"
        title = "COMPLETE"
        easygui.msgbox(msg,title)
    else:
        msg = "Cancelled."
        title = "CANCEL"
        easygui.msgbox(msg,title)


def change_status():
    print("e")
def change_priority():
    print("e")
def change_assignee():
    print("e")



#Main menu with all options available as a buttonbox
while True:
    msg = "Please choose an option"
    title = "MAIN MENU"                                                            
    choices = ["Print whole", "Update tasks", "Quit"]
    main_menu = easygui.buttonbox(msg,title,choices)

    #Checking which function to run based off input from main menu
    if main_menu == "Print whole":
        print_whole() 

    #A seperate menu if the user wishes to change the dictionary,
    #as to not overcrowd the buttonbox
    elif main_menu == "Update tasks":
        msg = "What do you want to do?"
        title = "CHOOSE"
        choices = ["Add a task", "Delete a task", "Back"]
        mini_menu = easygui.buttonbox(msg,title,choices)
        if mini_menu == "Add a task":
            add_task()
        elif mini_menu == "Delete a task":
            delete_task()
            
    else:
        break

msg = "Goodbye!"
title = "BYE"
easygui.msgbox(msg, title)