# Importing necessary libraries
import tkinter as tk  # For GUI-based application
from tkinter import messagebox

# Defining a class for the To-Do List application
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Creating a list to store tasks
        self.tasks = []

        # Creating a text entry widget to enter tasks
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        # Creating a button to add tasks
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack()

        # Creating a listbox to display tasks
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()

        # Creating a button to delete selected tasks
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack()

        # Load tasks from file if it exists
        self.load_tasks_from_file()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.update_tasks_file()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            self.tasks.remove(selected_task)
            self.update_task_listbox()
            self.update_tasks_file()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_tasks_file(self):
        # Write tasks to a text file named "tasks.txt"
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks_from_file(self):
        try:
            # Load tasks from "tasks.txt" file if it exists
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                self.update_task_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
