def task():
    tasks= []

    print("\n********* Welcome to Task Management App *********")

    total_task = int(input("\nHow many task you want to add? "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = " )
        tasks.append(task_name)

    print(f"\nYour tasks are\n{tasks}")

    while True:
        operations = int(input(f"\nEnter 1 to Add\nEnter 2 to Update\nEnter 3 to Delete\nEnter 4 to View\nEnter 5 to Close/Exit\nPlease Choose any number 1 to 5: "))

        if operations == 1:
            task_add = input("\nAdd your task: ")
            tasks.append(task_add)
            print(f"Your {task_add} task is successfully added")
            print(f"Updated Task list is {tasks}")

        elif operations == 2:
            print(tasks)
            task_update = input("\nWhich task you want to update: ")
            
            if task_update in tasks:
                task_update_new = input("Enter Task: ")
                index = tasks.index(task_update)
                tasks[index]=task_update_new
                print(f"Your {task_update} task is successfully replaced with {task_update_new}")
                print(f"Updated Task list is {tasks}")
            else:
                print(f"{task_update} is not exist in your Todo list")
                
        elif operations == 3:
            print(tasks)
            task_delete = input("\nWhich task you want to delete: ")
            
            if task_delete in tasks:
                index = tasks.index(task_delete)
                tasks.pop(index)
                print(f"Your {task_delete} task is successfully deleted")
                print(f"Updated Task list is {tasks}")
            else:
                print(f"{task_delete} is not exist in your Todo list")
        
        elif operations == 4:
            print(f"\nYour todo list is {tasks}")
        
        elif operations == 5:
            print("\nClosing the program........\n")
            break

        else:
            print("\nPlease choose write number between 1 to 5")

        
    

task()
