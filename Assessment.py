import easygui
tasks = {
    "T1":{
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "In Progress",
    },
    "T2":{
        "Title": "Implement Login Page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "Blocked",
    },
    "T3":{
        "Title": "Fix Navigation Menu",
        "Description": "Fix the navigation menu to be more user friendly",
        "Assignee": "None",
        "Priority": "1",
        "Status": "Not Started",
    },
    "T4":{
        "Title": "Add Payment Processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": "2",
        "Status": "In Progress",
    },
    "T5":{
        "Title": "Create an About Us Page",
        "Description": "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": "1",
        "Status": "Blocked",
    }
}

members = {
    "JSM":{
        "Name": "John Smith",
        "Email": "John@techvision.com"
    },
    "JLO":{
        "Name": "Jane Love",
        "Email": "Jane@techvision.com"
    },
    "BDI":{
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com"
        "Tasks Assigned": ""
    },
}

task_number = 0

def print_whole():
    """Displays entire nested dictionary in one msgbox by adding each
    element to an formatted output"""

    output = ""
    for item, item_info in tasks.items():
        output += (f"\ntask: {item} \n\n")
        for key in item_info:
            output += (f"{key}: {item_info[key]}  \n")
    title = "LIST"
    easygui.msgbox(output, title)

def search_option():
    """Allows the user to search a certain task and displays all
    aspects inside that title""" 

    output = "" 
    categories = [] 
    title = "SEARCH" 
    msg = "Click on the title you would like displayed" 
    #adding the movie titles from the dictionary to a list
    for titles in tasks: 
        categories.append(titles) 

    #getting the users choice
    search_title = easygui.buttonbox(msg, title, categories) 
    for items in tasks[search_title]: 
        output += f"\n{items}: {tasks[search_title][items]}" 
    title = f"{search_title}"
    easygui.msgbox(output, title) 


def add_entry():
    """Allows the user to add a new task to the database"""

    #getting all information for the new entry from user
    msg = "Enter a title for the task"
    title = easygui.enterbox(msg)
    msg = "Enter the a description of the task:"
    description = easygui.enterbox(msg)
    msg = "Enter select a task member to assign to the task:"
    assignee = easygui.buttonbox(msg)
    msg ="Enter the priority of the task (1-3):"
    priority = easygui.integerbox(msg)
    msg = "Enter the status of the task:"
    status = easygui.enterbox(msg)

    #add the new entry to the tasks dictionary
    for i in tasks:
        task_number += 1
    task_entry = "T" + f"{task_number}"
    tasks[f"T{task_entry}"] = {
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
    #adding the tasks from the dictionary to a list
    for task in tasks: 
        categories.append(task) 

    #getting the users choice
    deleted_task = easygui.buttonbox(msg, title, categories) 
    msg= f"Are you sure you want to delete {deleted_task}?"
    title = "CONFIRM"
    choices = ["Yes","No"]
    confirm = easygui.buttonbox(msg,title,choices)

    #confirming the choice
    if confirm == "Yes":
        del tasks[delete_task]
        msg = "Done!"
        title = "COMPLETE"
        easygui.msgbox(msg,title)
    else:
        msg = "Cancelled."
        title = "CANCEL"
        easygui.msgbox(msg,title)


#main menu with all options available as a buttonbox
while True:
    msg = "Please choose an option"
    title = "MAIN MENU"                                                            
    choices = ["Print whole", "Search", "Update tasks", "Quit"]
    main_menu = easygui.buttonbox(msg,title,choices)

    #checking which function to run based off input from main menu
    if main_menu == "Print Whole":
        print_whole() 
    elif main_menu == "Search":
        search_option()

    #a seperate menu if the user wishes to change the dictionary,
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