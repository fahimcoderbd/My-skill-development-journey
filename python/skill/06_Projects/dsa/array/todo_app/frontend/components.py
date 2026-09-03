#app ui components
import os
from typing import Callable

app_info = {
    'name':'ProTodo',
    'developer':'Fahim Abrar',
    'version':1.0
}

def banner(text:str):
    green()
    print("=="*20)
    white()
    print(text)
    green()

#colors for the ui
def green():
    print("\033[92m")

def red():
    print("\033[91m")

def white():
    print("\033[0m")

def cyan():
    print("\033[96m")

#welcome menu
def welcome_menu():
    banner(f"Welcome to {app_info['name']} \n version: {app_info['version']} \n developer: {app_info['developer']}")

#crud menu
def crud_menu():
    banner("Crud features")
    print("1. ➕ Add a task")
    print("2. 🗑️ Delete a task")
    print("3. ✏️ Edit a task")
    print("4. ✅ Complete a task")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def back(menu_choice: str, run_app_func: Callable):
    if menu_choice.lower() == "b":
        clear_screen()
        run_app_func()

#showing messages
def success(msg:str):
    green()
    print(msg)

def show_error(msg:str):
    red()
    print(msg)