import tkinter as tk
from tkinter import messagebox, IntVar
from tkcalendar import DateEntry
from datetime import datetime
from ttkthemes import ThemedStyle

class ReminderApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Task and Event Manager")
        self.window.minsize(width=500, height=400)

        # Task App components
        self.setup_reminder_app()

        # Event Manager components
        self.event_manager = EventManager(window, self)  # Pass a reference to ReminderApp
        self.hide_event_manager()

    def setup_reminder_app(self):
        # Calendar widget
        self.cal = DateEntry(self.window, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.cal.pack(pady=20)

        # Entry for reminder message
        self.message_entry = tk.Entry(self.window, width=30)
        self.message_entry.pack(pady=10)

        # Button to set reminder
        reminder_button = tk.Button(self.window, text="Set Task", command=self.set_reminder)
        reminder_button.pack(pady=10)

        # Task data list
        self.reminders = []  # Each reminder is now a dictionary with 'date', 'message', and 'status'

        # Show reminders button
        show_reminders_button = tk.Button(self.window, text="Show Tasks", command=self.show_reminders)
        show_reminders_button.pack(pady=5)

        # Task listbox
        self.reminder_list = tk.Canvas(self.window, bg='white', width=400, height=200)
        self.reminder_list.pack(pady=10)

        # Delete selected reminder button
        delete_button = tk.Button(self.window, text="Delete Selected Task", command=self.delete_selected_reminder)
        delete_button.pack(pady=5)

        # Show notification button
        show_notification_button = tk.Button(self.window, text="Show Notification", command=self.show_notification)
        show_notification_button.pack(pady=5)

    def toggle_event_manager(self):
        self.event_manager.toggle_visibility()

    def hide_event_manager(self):
        self.event_manager.hide()

    def set_reminder(self):
        date_selected = self.cal.get_date()
        reminder_date = datetime.strptime(date_selected.strftime("%m/%d/%y"), "%m/%d/%y").date()
        current_date = datetime.now().date()

        if reminder_date >= current_date:
            formatted_date = date_selected.strftime("%m/%d/%y")
            message = self.message_entry.get()  # Get the message from the entry
            status = IntVar()
            self.reminders.append({"date": formatted_date, "message": message, "status": status})
            messagebox.showinfo("Task Set", f"Task set for {formatted_date} with message: {message}")
            self.show_reminders()
        else:
            messagebox.showerror("Invalid Date", "Please select a valid date.")

    def show_reminders(self):
        self.reminder_list.delete("all")
        for i, reminder in enumerate(self.reminders):
            status_text = "Done" if reminder["status"].get() else "Not Done"
            check_button = tk.Checkbutton(self.reminder_list, text=f"{reminder['date']} - {reminder['message']} - {status_text}",
                                          variable=reminder["status"], onvalue=1, offvalue=0,
                                          command=lambda i=i: self.update_status(i))
            self.reminder_list.create_window(10, 20 * i, anchor=tk.W, window=check_button)

    def update_status(self, index):
        self.show_reminders()

    def delete_selected_reminder(self):
        selected_index = [i for i, reminder in enumerate(self.reminders) if reminder["status"].get()]
        for index in reversed(selected_index):
            self.reminders.pop(index)
        self.show_reminders()

    def show_notification(self):
        selected_index = [i for i, reminder in enumerate(self.reminders) if reminder["status"].get()]
        if selected_index:
            selected_reminder = self.reminders[selected_index[0]]
            status_text = "Done" if selected_reminder["status"].get() else "Not Done"
            messagebox.showinfo("Task", f"{selected_reminder['message']} - {selected_reminder['date']} - {status_text}")

class EventManager:
    def __init__(self, window, app):
        self.window = window
        self.app = app  # Reference to ReminderApp
        self.window.title("Dayminder")

        # Event data list
        self.events = []

        # Event frame
        self.event_frame = tk.LabelFrame(window, text="Event Manager")
        self.event_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Event listbox
        self.event_listbox = tk.Listbox(self.event_frame, selectmode=tk.SINGLE)
        self.event_listbox.pack(padx=10, pady=10, fill="both", expand=True)
        self.event_listbox.bind('<<ListboxSelect>>', self.show_event_details)

        # Event details label
        self.event_details_label = tk.Label(window, text="", wraplength=300)
        self.event_details_label.pack(padx=10, pady=5)

        # Add event button
        self.add_event_button = tk.Button(window, text="Add Event", command=self.add_event)

        # Call method to update listbox with existing events
        self.update_event_listbox()

    def toggle_visibility(self):
        current_state = self.event_frame.winfo_ismapped()
        if current_state:
            self.hide()
        else:
            self.show()

    def show(self):
        self.event_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.app.add_event_button.pack(padx=10, pady=5)

    def hide(self):
        self.event_frame.pack_forget()
        self.app.add_event_button.pack_forget()

    def add_event(self):
        # Function to add a new event
        add_window = tk.Toplevel(self.window)
        add_window.title("Add Event")

        # Entry for event title
        tk.Label(add_window, text="Event Title:").pack()
        event_title_entry = tk.Entry(add_window)
        event_title_entry.pack()

        # Entry for event date
        tk.Label(add_window, text="Event Date:").pack()
        event_date_entry = DateEntry(add_window, width=12, background="darkblue", foreground="white", borderwidth=2)
        event_date_entry.pack()

        # Button to save event
        save_button = tk.Button(add_window, text="Save", command=lambda: self.save_event(event_title_entry.get(), event_date_entry.get(), add_window))
        save_button.pack()

    def save_event(self, title, date, window):
        # Function to save a new event
        if title and date:
            self.events.append({"title": title, "date": date})
            window.destroy()  # Close the window after saving the event
            self.update_event_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter event title and date.")

    def update_event_listbox(self):
        # Function to update the event listbox
        self.event_listbox.delete(0, tk.END)
        for event in self.events:
            self.event_listbox.insert(tk.END, f"{event['title']} - {event['date']}")

    def show_event_details(self, event):
        # Function to display event details when selected
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.events[selected_index[0]]
            event_details = f"Title: {selected_event.get('title', '')}\n" \
                            f"Date: {selected_event.get('date', '')}"
            self.event_details_label.config(text=event_details)
        else:
            self.event_details_label.config(text="")

def main():
    window = tk.Tk()
    app = ReminderApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
