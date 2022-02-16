# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Naga Anusha,2.14.2022,Created Todolist script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
TASK = "Task"  # A Constant for storing the key
PRIORITY = "Priority"  # A Constant for storing the key

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
try:
    todo_file = open(objFile, "r")
    for index, row in enumerate(todo_file):
        if index > 0:
            row_values = row.split(",")
            dicRow = {
                TASK: row_values[0].strip(),
                PRIORITY: row_values[1].strip(),  # Saving the current data in Dictionary
            }
            lstTable.append(dicRow)
    todo_file.close()
except FileNotFoundError:
    print('file not found , will create one when saved')
print(lstTable)


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
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
    if strChoice.strip() == '1':
        print(TASK + ", " + PRIORITY)
        for dataRow in lstTable:
            print(dataRow[TASK] + ", " + dataRow[PRIORITY])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        newTask = input("enter new Task: ")
        newPriority = input("enter new priority:")
        dicRow = {
            TASK: newTask,
            PRIORITY: newPriority
        }
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        newTask = input("enter Task to remove: ")
        for dataRow in lstTable:
            if dataRow[TASK] == newTask:
                lstTable.remove(dataRow)
                print("Row removed")
        print(lstTable)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        print("The current items in the Todo are: ", lstTable)
        newFile = open("ToDoToDoList.txt", "w")
        newFile.write(TASK + ", " + PRIORITY + "\n")
        for dataRow in lstTable:
            newFile.write(dataRow[TASK] + "," + dataRow[PRIORITY] + "\n")
        print("Data saved to file! press the  enter key to return to the menu. ")
        newFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program
