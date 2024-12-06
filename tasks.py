import sys

'''
This will be a basic command line tool for managing tasks/To Dos

The classic ToDo list? - this is it. It will have CRUD operations and it will store data in a textfile/database using tinydb. 
For usage, I am going to create an alias in .zshrc to the script. There will be arguments for add, complete, update, and list tasks. I am thinking that the script will take the argument and then walk through which task to update or complete. List will just list, add will go through walkthrough for creating. 
Add can also just be given the task name as an argument and then it will add to db.



'''
try: 
    def printHelp():
        print("This is meant to be a script help screen")
        print("As we continue to update then this will change")
    
    
    def addTask(arg2):
        if (arg2 == ""):
            input("What task would you like to add?")
    
    def completeTask():
    #print the list of tasks - there should be an id number associated with each of the tasks that should be printed first. 
        input("What task would you like to add")

    def listTask():
    #here is where we will list the tasks 


    

    arg1 = sys.argv[1]
    arg2 = sys.argv[2] if len(sys.argv) > 2 else ""

    print(arg1 + " " + arg2)

    if(arg1 == "add"):
        addTask(arg2)

    elif(arg1 == "complete"):
        completeTask()

    elif(arg1 == "update"):
        updateTask(arg2)

    elif(arg1 == "list"):
        listTasks()

    else:
        printHelp()
        









except Exception as e:
    print(e)
    printHelp()
