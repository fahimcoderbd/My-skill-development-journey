class NotesApp:
    def __init__(self, path):
        self.path = path

    def show_error(self):
        print("\033[91mFile path not found. Please check folder.\033[0m")

    def add_note(self, data):
        try:
            with open(self.path, "a") as note:
                note.write(data + "\n")
            print("\033[92mNotes added successfully!\033[0m")

        except FileNotFoundError:
            self.show_error()

    def read_notes(self):
        try:
            with open(self.path, "r") as note:
                notes = note.read()
                print("\n📒 Your Notes:")
                print("-" * 30)
                print(notes if notes else "No notes found.")
                print("-" * 30)

        except FileNotFoundError:
            self.show_error()

    def show_menu(self):
        print("\n📘 Student Notes App")
        print("1. Read Notes")
        print("2. Add Note")
        print("3. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.read_notes()

            elif choice == "2":
                data = input("✍️ Enter your note: ")
                self.add_note(data)

            elif choice == "3":
                print("👋 Exiting app. Goodbye!")
                break

            else:
                print("\033[93mInvalid choice. Try again!\033[0m")


# --------- App Start ----------
path = "file_handling/practice/student_notes/notes.txt"
app = NotesApp(path)
app.run()
