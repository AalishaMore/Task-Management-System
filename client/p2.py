import requests
from datetime import datetime

def project_detail():
    while True:
        try:
            op = int(input("1 create, 2 read, 3 delete, and 4 exit "))
            if op == 1:
                name = input("Enter Project Name:")
                description = input("Enter Project description:")
                client = input("Enter Client Name:")
                end_date = input("Enter End Date: ")
                info = {
                    "name": name,
                    "description": description,
                    "client": client,
                    "end_date": end_date
                }
                url = "http://127.0.0.1:8000/api/projects/"
                res = requests.post(url, data=info)
                data = res.json()
                print(data)

            elif op == 2:
                url = "http://127.0.0.1:8000/api/projects/"
                res = requests.get(url)
                data = res.json()
                print(data)

            elif op == 3:
                id = int(input("Enter project ID to delete:"))
                url = f"http://127.0.0.1:8000/api/projects/{id}/"
                res = requests.delete(url)
                print("Response Status Code:", res.status_code)
                if res.status_code == 204:
                    print("Project deleted successfully.")
                elif res.status_code == 404:
                    print(f"Project with ID {id} not found.")
                else:
                    print("Failed to delete project or unexpected response.")

            elif op == 4:
                break

            else:
                print("Sorry, I don't understand")

        except Exception as e:
            print("Issue:", e)

project_detail()



def task_details():
    while True:
        try:
            op = int(input("1 create, 2 read, 3 delete, and 4 exit "))
            if op == 1:
                name = input("Enter Task Name:")
                description = input("Enter Task Description:")
                project_id = int(input("Enter Project ID for the Task:"))
                status = input("Enter Task Status (TODO, WIP, ONHOLD, DONE):")
                info = {
                    "name": name,
                    "description": description,
                    "project": project_id,
                    "status": status
                }
                url = "http://127.0.0.1:8000/api/tasks/"
                res = requests.post(url, data=info)
                data = res.json()
                print(data)

            elif op == 2:
                url = "http://127.0.0.1:8000/api/tasks/"
                res = requests.get(url)
                data = res.json()
                print(data)


            elif op == 3:
                id = int(input("Enter task ID to delete:"))
                url = f"http://127.0.0.1:8000/api/tasks/{id}/"
                res = requests.delete(url)
                print("Response Status Code:", res.status_code)
                if res.status_code == 204:
                    print("Task deleted successfully.")
                elif res.status_code == 404:
                    print(f"Task with ID {id} not found.")
                else:
                    print("Failed to delete task or unexpected response.")
               

            elif op == 4:
                break

            else:
                print("Sorry, I don't understand")

        except Exception as e:
            print("Issue:", e)

task_details()














