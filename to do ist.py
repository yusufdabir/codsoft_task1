import tkinter as tk

def print_todo_list():
    todo_list_text.delete(1.0, tk.END)
    if len(todo_list) == 0:
        todo_list_text.insert(tk.END, "No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            todo_list_text.insert(tk.END, f"{i}. {task}\n")

def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        print_todo_list()
        task_entry.delete(0, tk.END)
        create_task_buttons()  # Update task buttons

def remove_task(task_number):
    if 0 <= task_number < len(todo_list):
        removed_task = todo_list.pop(task_number)
        print_todo_list()
        status_label.config(text=f"Task '{removed_task}' removed from the to-do list.")
        create_task_buttons()  # Update task buttons
    else:
        status_label.config(text="Invalid task number.")

def edit_task(task_number):
    if 0 <= task_number < len(todo_list):
        edited_task = task_entry.get()
        todo_list[task_number] = edited_task
        print_todo_list()
        status_label.config(text=f"Task '{edited_task}' edited.")
        create_task_buttons()  # Update task buttons
    else:
        status_label.config(text="Invalid task number.")

# Main GUI window
root = tk.Tk()
root.title("To-Do List")

# To-Do List
todo_list = []

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Output frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

todo_list_text = tk.Text(output_frame, width=50, height=10)
todo_list_text.pack()

# Buttons for each task
task_buttons_frame = tk.Frame(output_frame)
task_buttons_frame.pack()

def create_task_buttons():
    for widget in task_buttons_frame.winfo_children():
        widget.destroy()  # Clear existing buttons

    for i, task in enumerate(todo_list):
        task_button = tk.Button(task_buttons_frame, text=f"Edit {i + 1}", command=lambda i=i: edit_task(i))
        task_button.grid(row=i, column=0, padx=5, pady=2)

        delete_button = tk.Button(task_buttons_frame, text=f"Delete {i + 1}", command=lambda i=i: remove_task(i))
        delete_button.grid(row=i, column=1, padx=5, pady=2)

create_task_buttons()

# Status label
status_label = tk.Label(root, text="", fg="red")
status_label.pack()

# Run the GUI main loop
root.mainloop()
