from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import ttk

def exit_program():
    exit()
    
def find_choice():
    global find_task_button, find_event_button, back_to_home_button, exit_button, from_where
    from_where = 'find'

    task_manager_button.grid_forget()
    event_manager_button.grid_forget()
    exit_button.grid_forget()

    label_for_space.grid_forget()
    label_for_space_3.grid_forget()
    label_for_space_4.grid_forget()
    label_for_space_5.grid_forget()

    find_task_button = Button(text='Find Task', command=find_task, bg='#f4ce14', fg='#000')
    find_task_button.grid(row=2, column=2)

    label_for_space_6 = Label(text='')
    label_for_space_6.grid(row=3, column=2)

    find_event_button = Button(text='Find Event', command=find_event, bg='#f4ce14', fg='#000')
    find_event_button.grid(row=4, column=2)

    label_for_space_7 = Label(text='')
    label_for_space_7.grid(row=5, column=2)

    back_to_home_button = Button(text='Back', command=back_first, bg='#f4ce14', fg='#000')
    back_to_home_button.grid(row=6, column=2)
    

def back_first():
    global add_task_button, add_event_button, delete_task_button, delete_event_button, back_to_home_button
    global task_manager_button, event_manager_button, exit_button

    if from_where == 'task':
        add_task_button.grid_forget()
        delete_task_button.grid_forget()
    elif from_where == 'event':
        add_event_button.grid_forget()
        delete_event_button.grid_forget()
    else :
        tasks_listbox.delete(0, END)
        for task in all_tasks:
            tasks_listbox.insert(END, task)
            
        events_listbox.delete(0, END)
        for event in all_events:
            events_listbox.insert(END, event)

    back_to_home_button.grid_forget()

    task_manager_button = Button(text='Task Manager', command=task_choice, bg='#f4ce14', fg='#000')
    task_manager_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    event_manager_button = Button(text='Event Manager', command=event_choice, bg='#f4ce14', fg='#000')
    event_manager_button.grid(row=4, column=2)
    
    find_button = Button(text='Find', command=find_choice, bg='#f4ce14', fg='#000')
    find_button.grid(row=6, column=2)
    
    exit_button = Button(text='Exit', command=exit_program, bg='#f4ce14', fg='#000')
    exit_button.grid(row=8, column=2)

def task_choice():
    global add_task_button, delete_task_button, back_to_home_button, from_where, exit_button

    from_where = 'task'

    task_manager_button.grid_forget()
    event_manager_button.grid_forget()
    exit_button.grid_forget()

    add_task_button = Button(text='Add New Task', command=add_new_task, bg='#f4ce14', fg='#000')
    add_task_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_task_button = Button(text='Delete Task', command=delete_task, bg='#f4ce14', fg='#000')
    delete_task_button.grid(row=4, column=2)

    label_for_space_2 = Label(text='')
    label_for_space_2.grid(row=5, column=2)

    back_to_home_button = Button(text='Back', command=back_first, bg='#f4ce14', fg='#000')
    back_to_home_button.grid(row=6, column=2)

def event_choice():
    global add_event_button, delete_event_button, back_to_home_button, from_where, exit_button

    from_where = 'event'

    task_manager_button.grid_forget()
    event_manager_button.grid_forget()
    exit_button.grid_forget()

    add_event_button = Button(text='Add New Event', command=add_new_event, bg='#f4ce14', fg='#000')
    add_event_button.grid(row=2, column=2)

    label_for_space = Label(text='')
    label_for_space.grid(row=3, column=2)

    delete_event_button = Button(text='Delete Event', command=delete_event, bg='#f4ce14', fg='#000')
    delete_event_button.grid(row=4, column=2)

    label_for_space_2 = Label(text='')
    label_for_space_2.grid(row=5, column=2)

    back_to_home_button = Button(text='Back', command=back_first, bg='#f4ce14', fg='#000')
    back_to_home_button.grid(row=6, column=2)

def add_new_task():
    add_task_window = Toplevel(window)
    add_task_window.title('Add New Task')
    add_task_window.attributes('-topmost', 'true')

    Label(add_task_window, text='Task time:').grid(row=1, column=0, pady=5)
    time_picker = ttk.Combobox(add_task_window, values=[f'{hour:02d}:{minute:02d}' for hour in range(24) for minute in range(0, 60, 15)])
    time_picker.set('12:00') 
    time_picker.grid(row=1, column=1, pady=5)

    Label(add_task_window, text='Task details:').grid(row=2, column=0, pady=5)
    task_entry = Entry(add_task_window, width=20)
    task_entry.grid(row=2, column=1, pady=5)

    def save_task():
        task_details = task_entry.get()
        task_time = time_picker.get()

        if task_details == '' or task_time == '':
            messagebox.showerror('Oops', 'Fill all the blank box!')
        else:
            task_text = f"{task_time} - {task_details}"
            tasks_listbox.insert(END, task_text)
            all_tasks.append(task_text) 
            add_task_window.destroy()
            back_first()

    save_button = Button(add_task_window, text='Save', command=save_task)
    save_button.grid(row=3, column=0, columnspan=2, pady=10)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        fix_delete = messagebox.askokcancel('Delete Event', 'Are you sure want to delete this task?')
        if fix_delete:
            deleted_task = tasks_listbox.get(selected_task_index)
            tasks_listbox.delete(selected_task_index)
            all_tasks.remove(deleted_task)
    back_first()

def add_new_event():
    add_event_window = Toplevel(window)
    add_event_window.title('Add New Event')
    add_event_window.attributes('-topmost', 'true')

    calendar = Calendar(add_event_window, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=0, column=0, columnspan=2, pady=10)

    Label(add_event_window, text='Event details:').grid(row=1, column=0, pady=5)
    event_entry = Entry(add_event_window, width=20)
    event_entry.grid(row=1, column=1, pady=5)

    def save_event():
        selected_date = calendar.get_date()
        event_details = event_entry.get()

        if event_details == '':
            messagebox.showerror('Oops', 'Fill all the blank box!')
        else:
            event_text = f"{selected_date} - {event_details}"
            events_listbox.insert(END, event_text)
            all_events.append(event_text)  # Append event to global list
            add_event_window.destroy()
            back_first()

    save_button = Button(add_event_window, text='Save', command=save_event)
    save_button.grid(row=2, column=0, columnspan=2, pady=10)

def delete_event():
    selected_event_index = events_listbox.curselection()
    if selected_event_index:
        fix_delete = messagebox.askokcancel('Delete Event', 'Are you sure want to delete this event?')
        if fix_delete:
            deleted_event = events_listbox.get(selected_event_index)
            events_listbox.delete(selected_event_index)
            all_events.remove(deleted_event)  
    back_first()

def find_task():
    find_window = Toplevel(window)
    find_window.title('Find Task')
    find_window.attributes('-topmost', 'true')

    search_label = Label(find_window, text='Search Task:')
    search_label.grid(row=0, column=0, pady=5)

    search_entry = Entry(find_window, width=20)
    search_entry.grid(row=0, column=1, pady=5)

    def filter_tasks():
        keyword = search_entry.get().lower()
        tasks_listbox.delete(0, END)  

        for task in all_tasks:
            if keyword in task.lower():
                tasks_listbox.insert(END, task)

    search_button = Button(find_window, text='Search', command=filter_tasks)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

def find_event():
    find_window = Toplevel(window)
    find_window.title('Find Event')
    find_window.attributes('-topmost', 'true')

    search_label = Label(find_window, text='Search Event:')
    search_label.grid(row=0, column=0, pady=5)

    search_entry = Entry(find_window, width=20)
    search_entry.grid(row=0, column=1, pady=5)

    def filter_events():
        keyword = search_entry.get().lower()
        events_listbox.delete(0, END)  

        for event in all_events:
            if keyword in event.lower():
                events_listbox.insert(END, event)

    search_button = Button(find_window, text='Search', command=filter_events)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

all_tasks = []
all_events = []

# window = Tk()
# window.title('Dayminder')
# window.config(padx=20, pady=50, bg='#F5F7F8')

add_task_button = None
delete_task_button = None
add_event_button = None
delete_event_button = None
back_to_home_button = None
from_where = ''

window = Tk()
window.title('Dayminder')
window.config(padx=20, pady=20, bg='#F5F7F8')


# Canvas

canvas = Canvas(width=532, height=152, highlightthickness=0, bg='#F5F7F8')
logo = PhotoImage(file='dayminder.png')
canvas.create_image(266, 76, image=logo)
canvas.grid(row=0, column=2)


# Button

task_manager_button = Button(text='Task Manager', command=task_choice, bg='#f4ce14', fg='#000')
task_manager_button.grid(row=2, column=2)

event_manager_button = Button(text='Event Manager', command=event_choice, bg='#f4ce14', fg='#000')
event_manager_button.grid(row=4, column=2)

exit_button = Button(text='Exit', command=exit_program, bg='#f4ce14', fg='#000')
exit_button.grid(row=8, column=2)

find_button = Button(text='Find', command=find_choice, bg='#f4ce14', fg='#000')
find_button.grid(row=6, column=2)


# Label

label_for_space = Label(text='')
label_for_space.grid(row=3, column=2)

label_for_space_3 = Label(text='')
label_for_space_3.grid(row=5, column=2)

task_label = Label(text='TASK', width=35, bg='#F5F7F8', font=('TkDefaultFont', '10', 'bold'))
task_label.grid(row=1, column=0, columnspan=2)

event_label = Label(text='EVENT', width=35, bg='#F5F7F8', font=('TkDefaultFont', '10', 'bold'))
event_label.grid(row=1, column=4, columnspan=2)

label_for_space_4 = Label(text='')
label_for_space_4.grid(row=3, column=2)

label_for_space_5 = Label(text='')
label_for_space_5.grid(row=3, column=3)

label_for_space_6 = Label(text='')
label_for_space_6.grid(row=7, column=2)
  

# Listbox

tasks_listbox = Listbox(window, selectmode=SINGLE, width=35)
tasks_listbox.grid(row=2, column=0, rowspan=5, columnspan=2)

events_listbox = Listbox(window, selectmode=SINGLE, width=35)  
events_listbox.grid(row=2, column=4, rowspan=5, columnspan=2)  


window.mainloop()
