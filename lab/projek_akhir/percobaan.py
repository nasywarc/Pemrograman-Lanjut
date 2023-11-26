from tkinter import *

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
    
    add_task_button = Button(text='Add New Task', command=...)
    add_task_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_task_button = Button(text='Delete Task')
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
    
    add_event_button = Button(text='Add New Event', command=...)
    add_event_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_event_button = Button(text='Delete Event')
    delete_event_button.grid(row=4, column=2)
    
    label_for_space_2 = Label(text='')
    label_for_space_2.grid(row=5, column=2)
    
    back_to_home_button = Button(text='Back', command=back_first)
    back_to_home_button.grid(row=6, column=2)


window = Tk()
window.title('Dayminder')
window.config(padx=50, pady=50)
# window.minsize(width=500, height=350)

canvas = Canvas(width=532, height=152, highlightthickness=0)
logo = PhotoImage(file='dayminder.png')
canvas.create_image(266, 76, image=logo)
canvas.grid(row=0, column=2)

add_task_button = None
delete_task_button = None
add_event_button = None
delete_event_button = None
back_to_home_button = None
from_where = ''

task_manager_button = Button(text='Task Manager', command=task_choice)
task_manager_button.grid(row=2, column=2)

label_for_space = Label(text='')
label_for_space.grid(row=3, column=2)

event_manager_button = Button(text='Event Manager', command=event_choice)
event_manager_button.grid(row=4, column=2)

window.mainloop()