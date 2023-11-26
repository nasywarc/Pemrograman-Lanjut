from tkinter import *
from tkcalendar import Calendar

def back_first():
    global add_task_button, add_event_button, delete_task_button, delete_event_button, back_to_home_button, task_manager_button, event_manager_button

    if from_where == 'task':
        add_task_button.grid_forget()
        delete_task_button.grid_forget()
    else:
        add_event_button.grid_forget()
        delete_event_button.grid_forget()

    back_to_home_button.grid_forget()

    task_manager_button = Button(text='Task Manager', command=task_choice)
    task_manager_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    event_manager_button = Button(text='Event Manager', command=event_choice)
    event_manager_button.grid(row=4, column=2)

def task_choice():
    global add_task_button, delete_task_button, back_to_home_button, from_where

    from_where = 'task'

    task_manager_button.grid_forget()
    event_manager_button.grid_forget()

    add_task_button = Button(text='Add New Task', command=add_new_task)
    add_task_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_task_button = Button(text='Delete Task', command=delete_task)
    delete_task_button.grid(row=4, column=2)

    label_for_space_2 = Label(text='')
    label_for_space_2.grid(row=5, column=2)

    back_to_home_button = Button(text='Back', command=back_first)
    back_to_home_button.grid(row=6, column=2)

def event_choice():
    global add_event_button, delete_event_button, back_to_home_button, from_where

    from_where = 'event'

    task_manager_button.grid_forget()
    event_manager_button.grid_forget()

    add_event_button = Button(text='Add New Event', command=add_new_event)
    add_event_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_event_button = Button(text='Delete Event', command=delete_event)
    delete_event_button.grid(row=4, column=2)

    label_for_space_2 = Label(text='')
    label_for_space_2.grid(row=5, column=2)

    back_to_home_button = Button(text='Back', command=back_first)
    back_to_home_button.grid(row=6, column=2)

def add_new_task():
    add_task_window = Toplevel(window)
    add_task_window.title('Add New Task')

    calendar = Calendar(add_task_window, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=0, column=0, columnspan=2, pady=10)

    Label(add_task_window, text='Task details:').grid(row=1, column=0, pady=5)
    task_entry = Entry(add_task_window, width=30)
    task_entry.grid(row=1, column=1, pady=5)

    def save_task():
        selected_date = calendar.get_date()
        task_details = task_entry.get()

        task_text = f"{selected_date} - {task_details}"
        tasks_listbox.insert(END, task_text)

        add_task_window.destroy()

    save_button = Button(add_task_window, text='Save', command=save_task)
    save_button.grid(row=2, column=0, columnspan=2, pady=10)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def add_new_event():
    add_event_window = Toplevel(window)
    add_event_window.title('Add New Event')

    calendar = Calendar(add_event_window, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=0, column=0, columnspan=2, pady=10)

    Label(add_event_window, text='Event details:').grid(row=1, column=0, pady=5)
    event_entry = Entry(add_event_window, width=30)
    event_entry.grid(row=1, column=1, pady=5)

    def save_event():
        selected_date = calendar.get_date()
        event_details = event_entry.get()

        event_text = f"{selected_date} - {event_details}"
        events_listbox.insert(END, event_text)

        add_event_window.destroy()

    save_button = Button(add_event_window, text='Save', command=save_event)
    save_button.grid(row=2, column=0, columnspan=2, pady=10)

def delete_event():
    selected_event_index = events_listbox.curselection()
    if selected_event_index:
        events_listbox.delete(selected_event_index)

window = Tk()
window.title('Dayminder')
window.config(padx=50, pady=50)

canvas = Canvas(width=532, height=152, highlightthickness=0)
logo = PhotoImage(file='dayminder.png')
canvas.create_image(266, 76, image=logo)
canvas.grid(row=0, column=2)

task_manager_button = Button(text='Task Manager', command=task_choice)
task_manager_button.grid(row=2, column=2)

label_for_space = Label(text='')
label_for_space.grid(row=3, column=2)

event_manager_button = Button(text='Event Manager', command=event_choice)
event_manager_button.grid(row=4, column=2)

add_task_button = None
delete_task_button = None
add_event_button = None
delete_event_button = None
back_to_home_button = None
from_where = ''

tasks_listbox = Listbox(window, selectmode=SINGLE)
tasks_listbox.grid(row=2, column=3, rowspan=5)

label_for_space_3 = Label(text='')
label_for_space_3.grid(row=3, column=2)

events_listbox = Listbox(window, selectmode=SINGLE)  
events_listbox.grid(row=2, column=4, rowspan=5)  

label_for_space_4 = Label(text='')
label_for_space_4.grid(row=3, column=3)  

window.mainloop()
