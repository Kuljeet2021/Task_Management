from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task

#Create a task
task1=create_task("Complete Your assignment","Finish TASK MANAGEMENT SYSTEM")
#Display the task
print("Task 1:",task1)
#Edit the task
edit_task(task1,new_title="Update Assignment",new_description="Reveiw and submite to Rashmi Mam")
#Display the Update task
print(" Update Task 1:",task1)
#Categorized the Task
categorize_task(task1,"Zappcode academy")
#Display Categorized the Task
print(" Categorized Task 1:",task1)
