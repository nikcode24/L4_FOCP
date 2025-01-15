# Task 3: Todo task with status and graph plot.

import matplotlib.pyplot as plt

todo_task = [
    "week 1 : class", 
    "week 2 : class", 
    "week 3 : class"
]
task_status = [
    "incomplete", 
    "complete", 
    "incomplete"
]

def addTask():
    task = input("please enter task: ")
    if task.strip() =="":
        print("please enter task")

    else:
        todo_task.append(task)
        task_status.append("incomplete")

def viewTask():
    if len(todo_task)==0:
        print("No task to Display")
    else:
        for i, (task, status) in enumerate(zip(todo_task, task_status), 1):
            print(f"{i} - {task}: {status}")


def updateTask():
    task_num = int(input("Enter a number:"))
    task_status [task_num - 1] == "complete"

def visualize():
    categories = ["complete","incomplete"]
    counts = [task_status.count("complete"),task_status.count("incomplete")]

    plt.bar(categories,counts)
    plt.title("Task bar")
    plt.xlabel("Task status")
    plt.ylabel("Counts")
    plt.show()


def userOperation():

    print("1 for addTask:\n2 for viewTask:\n3 for updateTask:\n4 for visualize:\n5 for exit:")

    user = int(input("Enter your Choice:"))

    if user == 1:
        addTask()
        
    elif user == 2:
        viewTask()
        
    elif user == 3:
        updateTask()
    
    elif user == 4:
        visualize()

    elif user == 5:
        exit()
    
    else:
        print("Please correct your input. ")
        

def main():
    while True:
        userOperation()

if __name__ == "__main__":
    main()
