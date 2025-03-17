from tkinter import *
from tkinter import ttk
from Manager import Manager
from Task import Status

manager = Manager()

def create_task():
    name = task_name_entry.get()
    description = task_description_entry.get()
    try:
        priority = int(task_priority_entry.get())
    except ValueError:
        print("Invalid input for priority. Please enter a valid integer.")
        return
    status = Status[task_status_var.get()]
    manager.create_Task(name, description, priority, status)
    update_task_table()
    task_name_entry.delete(0, END)
    task_description_entry.delete(0, END)
    task_priority_entry.delete(0, END)

def update_task_table():
    for row in task_table.get_children():
        task_table.delete(row)
    for task in manager.Tasks:
        tag = task.status.name.lower()
        task_table.insert("", "end", values=(task.priority, task.name, task.description, task.status.name), tags=(tag,))

def sort_treeview_column(treeview, col, reverse):
    l = [(treeview.set(k, col), k) for k in treeview.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        treeview.move(k, '', index)

    treeview.heading(col, command=lambda: sort_treeview_column(treeview, col, not reverse))

main_window = Tk()
main_window.rowconfigure(0, weight=1)
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.config(bg="#1f1f1f")
main_window.title("Task Manager")
main_window.geometry("1600x800")

frame1 = Frame(main_window, bg="#1f1f1f")
frame2 = Frame(main_window, bg="#1f1f1f")
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")

#------ FRAME 1
text = Label(frame1, text="Task Manager", fg="#d2d2d2", bg="#1f1f1f", state=NORMAL, font=("Arial", 48, "bold"))
text.pack()

Label(frame1, text="Task Name:", fg="#d2d2d2", bg="#1f1f1f" ,font=("Arial",20,"bold")).pack()
task_name_entry = Entry(frame1, bg="#3f3f3f", fg="#d2d2d2",width=40,font=("Arial",18))
task_name_entry.pack()

Label(frame1, text="Description:", fg="#d2d2d2", bg="#1f1f1f",font=("Arial",20,"bold")).pack()
task_description_entry = Entry(frame1, bg="#3f3f3f", fg="#d2d2d2",width=40,font=("Arial",18))
task_description_entry.pack()

Label(frame1, text="Priority:", fg="#d2d2d2", bg="#1f1f1f",font=("Arial",20,"bold")).pack()
task_priority_entry = Entry(frame1, bg="#3f3f3f", fg="#d2d2d2",width=40,font=("Arial",18))
task_priority_entry.pack()

Label(frame1, text="Status:", fg="#d2d2d2", bg="#1f1f1f",font=("Arial",20,"bold")).pack()
task_status_var = StringVar(frame1)
task_status_var.set("TODO")
task_status_menu = OptionMenu(frame1, task_status_var, *[status.name for status in Status])
task_status_menu.configure(bg="#1f1f1f",borderwidth=0,relief="solid",fg="#d2d2d2",font=("Arial",18))

task_status_menu.pack()

create_task_button = Button(frame1, text="Create Task", command=create_task, bg="#1f1f1f", fg="#d2d2d2",font=("Arial",20,"bold"))
create_task_button.pack(pady=20)

#------ FRAME 2
style = ttk.Style()
style.configure("Treeview", font=('Arial', 15, 'bold'))
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'), background="#1f1f1f")

task_table = ttk.Treeview(frame2, columns=("Priority", "Name", "Description", "Status"), show="headings", style="Treeview")
task_table.heading("Priority", text="Priority", anchor=CENTER,command=lambda: sort_treeview_column(task_table, "Priority", False))
task_table.heading("Name", text="Name", anchor=CENTER,command=lambda: sort_treeview_column(task_table, "Name", False))
task_table.heading("Description", text="Description", anchor=CENTER,command=lambda: sort_treeview_column(task_table, "Description", False))
task_table.heading("Status", text="Status", anchor=CENTER,command=lambda: sort_treeview_column(task_table, "Status", False))

# Set column widths
task_table.column("Priority", width=50, anchor=CENTER)
task_table.column("Name", width=150, anchor=CENTER)
task_table.column("Description", width=400, anchor=CENTER)
task_table.column("Status", width=50, anchor=CENTER)

# Configure tags for different statuses
task_table.tag_configure('todo', background='yellow', font=('Arial', 12, 'bold'))
task_table.tag_configure('blocked', background='red', font=('Arial', 12, 'bold'))
task_table.tag_configure('inprogress', background='lightblue', font=('Arial', 12, 'bold'))
task_table.tag_configure('completed', background='green', font=('Arial', 12, 'bold'))

task_table.pack(fill=BOTH, expand=True)

main_window.mainloop()
