import requests

def get_emp_todo(emp_id):
    TODO_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    USER_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    # Get the JSON of TODOS - DONE
    # Get TOTAL NUMBER of todos - DONE
    # Get COMPLETED NUMBER of todos - DONE
    # Get THE NAME of the employee - DONE 

    # GET THE TITLES OF THE COMPLETED TASKS
    # AND PRINT THEM ALL OUT ON STDOUT
    # EACH TASKS SHOULD BE PRINTED ON A NEW LINE
    
    emp_name = requests.get(USER_URL).json()["name"]
    emp_todos = requests.get(TODO_URL).json()
    emp_total_todos = len(emp_todos)
    emp_completed_todos = 0
    for todo in emp_todos:
        if todo["completed"] is True:
            emp_completed_todos += 1
    print(f"Employee {emp_name} From total todos of {emp_total_todos}, {emp_completed_todos} tasks have been done")


get_emp_todo(3)