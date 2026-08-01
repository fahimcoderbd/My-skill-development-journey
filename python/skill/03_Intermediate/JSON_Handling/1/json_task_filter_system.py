import json

def load_tasks(file):
    with open(file, 'r') as f:
        return json.load(f)

def show_incomplete(tasks):
    for task in tasks:
        if not task["completed"]:
            print(task["title"])

def show_high_priority(tasks):
    for task in tasks:
        if task["priority"] == "high":
            print(task["title"])

def count_tasks(tasks):
    completed = 0
    incomplete = 0

    for task in tasks:
        if task["completed"]:
            completed += 1
        else:
            incomplete += 1

    print(f"Completed: {completed}")
    print(f"Incomplete: {incomplete}")


# main
tasks = load_tasks("json/tasks.json")

print("Incomplete Tasks:")
show_incomplete(tasks)

print("\nHigh Priority Tasks:")
show_high_priority(tasks)

print("\nTask Stats:")
count_tasks(tasks)