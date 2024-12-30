import sys
import sqlite3
'''
This will be a basic command line tool for managing tasks/To Dos

The classic ToDo list? - this is it. It will have CRUD operations and it will store data in a textfile/database using tinydb. 
For usage, I am going to create an alias in .zshrc to the script. There will be arguments for add, complete, update, and list tasks. I am thinking that the script will take the argument and then walk through which task to update or complete. List will just list, add will go through walkthrough for creating. 
Add can also just be given the task name as an argument and then it will add to db.



'''
try:
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()

    sql_table = '''CREATE TABLE IF NOT EXISTS tasks(description TEXT)'''
    cursor.execute(sql_table)
    def printHelp():
        print("This is meant to be a script help screen")
        print("As we continue to update then this will change")
    
    def getTasks():
        list_tasks = '''SELECT description FROM tasks'''
        cursor.execute(list_tasks)

        tasks = cursor.fetchall()

        return tasks


    def listTask():
    #here is where we will list the tasks 
        tasks = getTasks()
        for index, task in enumerate(tasks):
            print(f"Task Number: {index}: {task[0]}")

    def updateTask(arg2):
        if (arg2 == ""):
            listTask()
            taskIndex = input("What task would you like to update?")
        else:
            taskIndex = arg2
        
        newTask = input("What would you like to update the task to?")
            
        tasks = getTasks()
        print(type(taskIndex))
        task = tasks[int(taskIndex)][0]
        print (task)
        print(type(task))
        update_sql = '''
            UPDATE tasks
            SET description = ?
            WHERE description = ?
            '''
        cursor.execute(update_sql, (newTask, task))
        con.commit()
        con.close()
             
    def addTask(arg2):
        if (arg2 == ""):
            listTask()
            task = input("What task would you like to add? ")        
            if(task == ""):
                printHelp()
            else: #adding a check to see if the task already exists
                add_task = '''INSERT INTO tasks(description) VALUES(?)'''
                cursor.execute(add_task, (task,))
                con.commit()
                con.close()
    def completeTask():
    #print the list of tasks - there should be an id number associated with each of the tasks that should be printed first. 
        listTask()
        taskIndex = input("What task would you like to complete?")
        tasks = getTasks()
        task = tasks[int(taskIndex)][0]
        delete_sql = '''DELETE FROM tasks WHERE description = ?'''

        cursor.execute(delete_sql, (task,))
        con.commit()
        con.close()

        print(f"Task: {task} completed.")


    
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
        listTask()

    else:
        printHelp()
        









except Exception as e:
    print(e)
    con.close()
    printHelp() #this wont be seen because it is outside of the try
