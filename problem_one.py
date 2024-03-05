import requests

def get_emp_todo(emp_id):

    TODO_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    USER_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    
    emp_todo = requests.get(TODO_URL).json()
    emp_data = requests.get(USER_URL).json()
    
    # Get json from URL -- DONE
    # Get total  number of todos from JSON -- DONE
    # Get number of completed todos -- Done
    # Get the name of the employee -- DONE 

    # LIST ALL THE TASKS THE EMPLOYEE COMPLETED
    # EACH TASK HAS TO BE PRINTED ON A NEW LINE

    emp_name = emp_data["name"]
    total_todos = len(emp_todo)
    completed_todos = 0

    for todo in emp_todo:
        if todo["completed"]:
            completed_todos += 1
    print(f"Employee {emp_name} , out of {total_todos} total tasks, has completed {completed_todos} tasks")

get_emp_todo(1)