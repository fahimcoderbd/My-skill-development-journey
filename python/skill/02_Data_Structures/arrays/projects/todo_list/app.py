# ==========================
# Simple Todo App
# ==========================

# Store todos
todos = []


# Add a task
def add_task(task_name):
    todos.append(task_name)
    return f'"{task_name}" added successfully!'


# Show all tasks
def show_todos():
    if not todos:
        return "No todos found."

    result = "\n===== YOUR TODOS =====\n"

    for i, task in enumerate(todos, start=1):
        result += f"{i}. {task}\n"

    return result


# Delete a task
def delete_task(task_name):
    if not todos:
        return "No todos found."

    if task_name in todos:
        todos.remove(task_name)
        return f'"{task_name}" deleted successfully!'

    return f'"{task_name}" not found.'


# Complete a task
def complete_task(task_name):
    result = delete_task(task_name)

    if "deleted successfully" in result:
        return f'"{task_name}" completed successfully!'

    return result


# Search for a task
def search_task(task_name):
    if task_name in todos:
        return f'"{task_name}" found successfully!'

    return f'"{task_name}" not found.'


# ==========================
# Testing
# ==========================

print(add_task("Sleep"))
print(add_task("Coding"))
print(add_task("Gym"))

print(show_todos())

print(search_task("Coding"))
print(search_task("Reading"))

print(delete_task("Sleep"))

print(show_todos())

print(complete_task("Coding"))

print(show_todos())

print(search_task("Coding"))