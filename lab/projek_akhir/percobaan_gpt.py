from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

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
    global task_manager_button, event_manager_button, exit_button, edit_task_button, edit_event_button

    if from_where == 'task':
        add_task_button.grid_forget()
        delete_task_button.grid_forget()
        edit_task_button.grid_forget()
    elif from_where == 'event':
        add_event_button.grid_forget()
        delete_event_button.grid_forget()
        edit_event_button.grid_forget()
    else:
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
    global add_task_button, delete_task_button, back_to_home_button, edit_task_button, from_where, exit_button

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

    edit_task_button = Button(text='Edit Task', command=edit_task, bg='#f4ce14', fg='#000')
    edit_task_button.grid(row=6, column=2)
    
    label_for_space_3 = Label(text='')
    label_for_space_3.grid(row=7, column=2)

    back_to_home_button = Button(text='Back', command=back_first, bg='#f4ce14', fg='#000')
    back_to_home_button.grid(row=8, column=2)

def event_choice():
    global add_event_button, delete_event_button, back_to_home_button, edit_event_button, from_where, exit_button

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

    edit_event_button = Button(text='Edit Event', command=edit_event, bg='#f4ce14', fg='#000')
    edit_event_button.grid(row=6, column=2)
    
    label_for_space_3 = Label(text='')
    label_for_space_3.grid(row=7, column=2)

    back_to_home_button = Button(text='Back', command=back_first, bg='#f4ce14', fg='#000')
    back_to_home_button.grid(row=8, column=2)

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

    Label(add_event_window, text='Select Categories:').grid(row=2, column=0, pady=5)

    category_var_1 = IntVar()
    category_checkbutton_1 = Checkbutton(add_event_window, text='General', variable=category_var_1)
    category_checkbutton_1.grid(row=2, column=1, sticky='w')

    category_var_2 = IntVar()
    category_checkbutton_2 = Checkbutton(add_event_window, text='Education', variable=category_var_2)
    category_checkbutton_2.grid(row=3, column=1, sticky='w')
    
    category_var_3 = IntVar()
    category_checkbutton_3 = Checkbutton(add_event_window, text='Personal Work', variable=category_var_3)
    category_checkbutton_3.grid(row=4, column=1, sticky='w')
    
    category_var_4 = IntVar()
    category_checkbutton_4 = Checkbutton(add_event_window, text='Projects', variable=category_var_4)
    category_checkbutton_4.grid(row=5, column=1, sticky='w')
    
    category_var_5 = IntVar()
    category_checkbutton_5 = Checkbutton(add_event_window, text='Meetings', variable=category_var_5)
    category_checkbutton_5.grid(row=6, column=1, sticky='w')
    
    category_var_6 = IntVar()
    category_checkbutton_6 = Checkbutton(add_event_window, text='Holidays', variable=category_var_6)
    category_checkbutton_6.grid(row=7, column=1, sticky='w')
    
    category_var_7 = IntVar()
    category_checkbutton_7 = Checkbutton(add_event_window, text='Health', variable=category_var_7)
    category_checkbutton_7.grid(row=8, column=1, sticky='w')
    
    category_var_8 = IntVar()
    category_checkbutton_8 = Checkbutton(add_event_window, text='Social Events', variable=category_var_8)
    category_checkbutton_8.grid(row=9, column=1, sticky='w')
    
    category_var_9 = IntVar()
    category_checkbutton_9 = Checkbutton(add_event_window, text='Financial', variable=category_var_9)
    category_checkbutton_9.grid(row=10, column=1, sticky='w')
    

    def save_event():
        selected_date = calendar.get_date()
        event_details = event_entry.get()

        if event_details == '':
            messagebox.showerror('Oops', 'Fill all the blank box!')
        else:
            selected_categories = []
            if category_var_1.get():
                selected_categories.append(category_checkbutton_1['text'])
            if category_var_2.get():
                selected_categories.append(category_checkbutton_2['text'])
            if category_var_3.get():
                selected_categories.append(category_checkbutton_3['text'])
            if category_var_4.get():
                selected_categories.append(category_checkbutton_4['text'])
            if category_var_5.get():
                selected_categories.append(category_checkbutton_5['text'])
            if category_var_6.get():
                selected_categories.append(category_checkbutton_6['text'])
            if category_var_7.get():
                selected_categories.append(category_checkbutton_7['text'])
            if category_var_8.get():
                selected_categories.append(category_checkbutton_8['text'])
            if category_var_9.get():
                selected_categories.append(category_checkbutton_9['text'])
            if len(selected_categories) == 0:
                selected_categories.append(category_checkbutton_1['text'])
            

            event_text = f"{selected_date} - {event_details} ({', '.join(selected_categories)})"
            events_listbox.insert(END, event_text)
            all_events.append(event_text)
            add_event_window.destroy()
            back_first()

    save_button = Button(add_event_window, text='Save', command=save_event)
    save_button.grid(row=12, column=0, columnspan=2, pady=10)

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

def edit_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_to_edit = tasks_listbox.get(selected_task_index)
        edit_task_window = Toplevel(window)
        edit_task_window.title('Edit Task')
        edit_task_window.attributes('-topmost', 'true')

        # Extracting time and details from the selected task
        try:
            task_time, task_details = extract_task_info(task_to_edit)
        except ValueError:
            messagebox.showerror('Error', 'Invalid task format')
            return

        Label(edit_task_window, text='Task time:').grid(row=1, column=0, pady=5)
        time_picker = ttk.Combobox(edit_task_window, values=[f'{hour:02d}:{minute:02d}' for hour in range(24) for minute in range(0, 60, 15)])
        time_picker.set(task_time) 
        time_picker.grid(row=1, column=1, pady=5)

        Label(edit_task_window, text='Task details:').grid(row=2, column=0, pady=5)
        task_entry = Entry(edit_task_window, width=20)
        task_entry.insert(0, task_details)
        task_entry.grid(row=2, column=1, pady=5)

        def save_edited_task():
            new_task_details = task_entry.get()
            new_task_time = time_picker.get()

            if new_task_details == '' or new_task_time == '':
                messagebox.showerror('Oops', 'Fill all the blank boxes!')
            else:
                edited_task_text = f"{new_task_time} - {new_task_details}"
                tasks_listbox.delete(selected_task_index)
                tasks_listbox.insert(selected_task_index, edited_task_text)
                all_tasks[selected_task_index] = edited_task_text
                edit_task_window.destroy()
                back_first()

        save_button = Button(edit_task_window, text='Save', command=save_edited_task)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

# def edit_event():
#     selected_event_index = events_listbox.curselection()
#     if selected_event_index:
#         event_to_edit = events_listbox.get(selected_event_index)
#         edit_event_window = Toplevel(window)
#         edit_event_window.title('Edit Event')
#         edit_event_window.attributes('-topmost', 'true')

#         # Extracting date, details, and categories from the selected event
#         try:
#             event_date, event_details, event_categories = extract_event_info(event_to_edit)
#         except ValueError:
#             messagebox.showerror('Error', 'Invalid event format')
#             return

#         calendar = Calendar(edit_event_window, selectmode='day', date_pattern='yyyy-mm-dd')
#         calendar.set_date(event_date)
#         calendar.grid(row=0, column=0, columnspan=2, pady=10)

#         Label(edit_event_window, text='Event details:').grid(row=1, column=0, pady=5)
#         event_entry = Entry(edit_event_window, width=20)
#         event_entry.insert(0, event_details)
#         event_entry.grid(row=1, column=1, pady=5)

#         Label(edit_event_window, text='Select Categories:').grid(row=2, column=0, pady=5)

#         category_var_1 = IntVar()
#         category_checkbutton_1 = Checkbutton(edit_event_window, text='General', variable=category_var_1)
#         category_checkbutton_1.grid(row=2, column=1, sticky='w')

#         category_var_1 = IntVar()
#         category_checkbutton_1 = Checkbutton(edit_event_window, text='General', variable=category_var_1)
#         category_checkbutton_1.grid(row=2, column=1, sticky='w')

#         category_var_2 = IntVar()
#         category_checkbutton_2 = Checkbutton(edit_event_window, text='Education', variable=category_var_2)
#         category_checkbutton_2.grid(row=3, column=1, sticky='w')
        
#         category_var_3 = IntVar()
#         category_checkbutton_3 = Checkbutton(edit_event_window, text='Personal Work', variable=category_var_3)
#         category_checkbutton_3.grid(row=4, column=1, sticky='w')
        
#         category_var_4 = IntVar()
#         category_checkbutton_4 = Checkbutton(edit_event_window, text='Projects', variable=category_var_4)
#         category_checkbutton_4.grid(row=5, column=1, sticky='w')
        
#         category_var_5 = IntVar()
#         category_checkbutton_5 = Checkbutton(edit_event_window, text='Meetings', variable=category_var_5)
#         category_checkbutton_5.grid(row=6, column=1, sticky='w')
        
#         category_var_6 = IntVar()
#         category_checkbutton_6 = Checkbutton(edit_event_window, text='Holidays', variable=category_var_6)
#         category_checkbutton_6.grid(row=7, column=1, sticky='w')
        
#         category_var_7 = IntVar()
#         category_checkbutton_7 = Checkbutton(edit_event_window, text='Health', variable=category_var_7)
#         category_checkbutton_7.grid(row=8, column=1, sticky='w')
        
#         category_var_8 = IntVar()
#         category_checkbutton_8 = Checkbutton(edit_event_window, text='Social Events', variable=category_var_8)
#         category_checkbutton_8.grid(row=9, column=1, sticky='w')
        
#         category_var_9 = IntVar()
#         category_checkbutton_9 = Checkbutton(edit_event_window, text='Financial', variable=category_var_9)
#         category_checkbutton_9.grid(row=10, column=1, sticky='w')

#         def save_edited_event():
#             selected_date = calendar.get_date()
#             new_event_details = event_entry.get()

#             if new_event_details == '':
#                 messagebox.showerror('Oops', 'Fill all the blank boxes!')
#             else:
#                 edited_event_text = f"{selected_date} - {new_event_details} ({', '.join(event_categories)})"
#                 events_listbox.delete(selected_event_index)
#                 events_listbox.insert(selected_event_index, edited_event_text)
#                 all_events[selected_event_index] = edited_event_text
#                 edit_event_window.destroy()
#                 back_first()

#         save_button = Button(edit_event_window, text='Save', command=save_edited_event)
#         save_button.grid(row=12, column=0, columnspan=2, pady=10)

from datetime import datetime

# ...

def edit_event():
    selected_event_index = events_listbox.curselection()
    if selected_event_index:
        event_to_edit = events_listbox.get(selected_event_index)
        edit_event_window = Toplevel(window)
        edit_event_window.title('Edit Event')
        edit_event_window.attributes('-topmost', 'true')

        # Extracting date, details, and categories from the selected event
        try:
            event_date, event_details, event_categories = extract_event_info(event_to_edit)
        except ValueError:
            messagebox.showerror('Error', 'Invalid event format')
            return

        calendar = Calendar(edit_event_window, selectmode='day', date_pattern='yyyy-mm-dd')
        calendar_date = datetime.strptime(event_date, '%Y-%m-%d')
        calendar.set_date(calendar_date)
        calendar.grid(row=0, column=0, columnspan=2, pady=10)

        Label(edit_event_window, text='Event details:').grid(row=1, column=0, pady=5)
        event_entry = Entry(edit_event_window, width=20)
        event_entry.insert(0, event_details)
        event_entry.grid(row=1, column=1, pady=5)

        Label(edit_event_window, text='Select Categories:').grid(row=2, column=0, pady=5)

        category_var_1 = IntVar()
        category_checkbutton_1 = Checkbutton(edit_event_window, text='General', variable=category_var_1)
        category_checkbutton_1.grid(row=2, column=1, sticky='w')

        category_var_1 = IntVar()
        category_checkbutton_1 = Checkbutton(edit_event_window, text='General', variable=category_var_1)
        category_checkbutton_1.grid(row=2, column=1, sticky='w')

        category_var_2 = IntVar()
        category_checkbutton_2 = Checkbutton(edit_event_window, text='Education', variable=category_var_2)
        category_checkbutton_2.grid(row=3, column=1, sticky='w')
        
        category_var_3 = IntVar()
        category_checkbutton_3 = Checkbutton(edit_event_window, text='Personal Work', variable=category_var_3)
        category_checkbutton_3.grid(row=4, column=1, sticky='w')
        
        category_var_4 = IntVar()
        category_checkbutton_4 = Checkbutton(edit_event_window, text='Projects', variable=category_var_4)
        category_checkbutton_4.grid(row=5, column=1, sticky='w')
        
        category_var_5 = IntVar()
        category_checkbutton_5 = Checkbutton(edit_event_window, text='Meetings', variable=category_var_5)
        category_checkbutton_5.grid(row=6, column=1, sticky='w')
        
        category_var_6 = IntVar()
        category_checkbutton_6 = Checkbutton(edit_event_window, text='Holidays', variable=category_var_6)
        category_checkbutton_6.grid(row=7, column=1, sticky='w')
        
        category_var_7 = IntVar()
        category_checkbutton_7 = Checkbutton(edit_event_window, text='Health', variable=category_var_7)
        category_checkbutton_7.grid(row=8, column=1, sticky='w')
        
        category_var_8 = IntVar()
        category_checkbutton_8 = Checkbutton(edit_event_window, text='Social Events', variable=category_var_8)
        category_checkbutton_8.grid(row=9, column=1, sticky='w')
        
        category_var_9 = IntVar()
        category_checkbutton_9 = Checkbutton(edit_event_window, text='Financial', variable=category_var_9)
        category_checkbutton_9.grid(row=10, column=1, sticky='w')

        def save_edited_event():
            selected_date = calendar.get_date()
            new_event_details = event_entry.get()

            if new_event_details == '':
                messagebox.showerror('Oops', 'Fill all the blank boxes!')
            else:
                edited_event_text = f"{selected_date} - {new_event_details} ({', '.join(event_categories)})"
                events_listbox.delete(selected_event_index)
                events_listbox.insert(selected_event_index, edited_event_text)
                all_events[selected_event_index] = edited_event_text
                edit_event_window.destroy()
                back_first()

        save_button = Button(edit_event_window, text='Save', command=save_edited_event)
        save_button.grid(row=12, column=0, columnspan=2, pady=10)


    
def extract_task_info(task_text):
    # Task text format: "hh:mm - Task details"
    task_time, task_details = task_text.split(' - ', 1)
    return task_time, task_details

def extract_event_info(event_text):
    # Event text format: "yyyy-mm-dd - Event details (Category 1, Category 2, ...)"
    event_date, rest = event_text.split(' - ', 1)
    event_details, categories_text = rest.split(' (', 1)
    # Removing the closing parenthesis from categories_text
    categories_text = categories_text.rstrip(')')
    event_categories = [category.strip() for category in categories_text.split(',')]
    return event_date, event_details, event_categories


all_tasks = []
all_events = []

add_task_button = None
delete_task_button = None
edit_task_button = None
add_event_button = None
delete_event_button = None
edit_event_button = None
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
