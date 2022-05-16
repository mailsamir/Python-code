# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SAbad,05.15.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

try:     # Error handling introduced to check for the file
    strFile = open(objFile, "r")
    for row in strFile:
        t, p = row.split(",")
        dicRow = {"Task": t, "Priority": p.strip()}
        lstTable.append(dicRow)
        print(dicRow["Task"] + ',' + dicRow["Priority"])
    strFile.close()
except:       # if file not found
    print("File not found. New file will be created when you save.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Task" + '|' + "Priority")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a new task:")
        strPriority = input("Enter the priority:")
        dicRow={"Task":strTask, "Priority":strPriority}
        lstTable.append(dicRow)
        print("Task" + '|' + "Priority")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"])
    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strtaskR = input("Enter the task to be removed:")
        for row in lstTable:
            if row["Task"].lower() == strtaskR.lower():
                lstTable.remove(row)
                print("Task removed")
                print(lstTable)
            else:
                print("Task not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        strFile = open(objFile, "w")
        for row in lstTable:
            strFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        strFile.close()
        print("Tasks successfully saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("You have exited the program!")
        break  # and Exit the program

    else:
        print("Please select numbers from 1-5")
