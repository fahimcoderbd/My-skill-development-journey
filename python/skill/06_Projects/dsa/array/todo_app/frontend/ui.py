from components import crud_menu,welcome_menu,show_error,cyan,green,back

app_running = True

def run():
    while app_running:
        welcome_menu()
        crud_menu()
        print("\n") #line breaking
        # taking menu choice from user with icons and improved back handling
        green()
        print("Press Enter b to back to menu (🔙)")
        cyan()
        user = input("Enter a choice (e.g. 1 ➕, 2 ✏️, 3 🗑️): ")
        # if user just presses enter, go back to menu loop
        back(user, run)

if __name__ == "__main__":
    run()
