import tkinter as tk
from tkinter import messagebox, IntVar
from tkcalendar import DateEntry
from datetime import datetime

class ReminderApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Task and Event Manager")
        self.window.minsize(width=500, height=400)

        # Initialize reminders attribute
        self.reminders = []

        # Task App components
        self.setup_reminder_app()

        # Event Manager components
        self.event_manager = EventManager(window)

    def setup_reminder_app(self):
        # Button to show Task components
        task_button = tk.Button(self.window, text="Task", command=self.show_task_components)
        task_button.pack(pady=20)

        # Button to show Event Manager components
        event_manager_button = tk.Button(self.window, text="Event Manager", command=self.show_event_manager_components)
        event_manager_button.pack(pady=20)

        # Frame to contain components of Task and Event Manager
        self.content_frame = tk.Frame(self.window)
        self.content_frame.pack()

    def show_task_components(self):
        # Clear the content frame
        self.destroy_content_frame()

        # Hide Event Manager components
        self.event_manager.hide_components()

        # Add Task components
        self.cal = DateEntry(self.content_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.cal.pack(pady=20)

        self.message_entry = tk.Entry(self.content_frame, width=30)
        self.message_entry.pack(pady=10)

        reminder_button = tk.Button(self.content_frame, text="Set Task", command=self.set_reminder)
        reminder_button.pack(pady=10)

        show_reminders_button = tk.Button(self.content_frame, text="Show Tasks", command=self.show_reminders)
        show_reminders_button.pack(pady=5)

        self.reminder_list = tk.Canvas(self.content_frame, bg='white', width=400, height=200)
        self.reminder_list.pack(pady=10)

        delete_button = tk.Button(self.content_frame, text="Delete Selected Task", command=self.delete_selected_reminder)
        delete_button.pack(pady=5)

        show_notification_button = tk.Button(self.content_frame, text="Show Notification", command=self.show_notification)
        show_notification_button.pack(pady=5)

    def show_event_manager_components(self):
        # Clear the content frame
        self.destroy_content_frame()

        # Add Event Manager components
        self.event_manager.show_components()

    def destroy_content_frame(self):
        # Destroy widgets inside content_frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def set_reminder(self):
        # Check if self.reminders is not defined, initialize it
        if not hasattr(self, 'reminders'):
            self.reminders = []

        date_selected = self.cal.get_date()
        reminder_date = datetime.strptime(date_selected.strftime("%m/%d/%y"), "%m/%d/%y").date()
        current_date = datetime.now().date()

        if reminder_date >= current_date:
            formatted_date = date_selected.strftime("%m/%d/%y")
            message = self.message_entry.get()
            status = tk.IntVar()
            self.reminders.append({"date": formatted_date, "message": message, "status": status})
            messagebox.showinfo("Task Set", f"Task set for {formatted_date} with message: {message}")
            self.show_reminders()
        else:
            messagebox.showerror("Invalid Date", "Please select a valid date.")

    def show_reminders(self):
        self.reminder_list.delete("all")
        for i, reminder in enumerate(self.reminders):
            status_text = "Done" if reminder["status"].get() else "Not Done"
            check_button = tk.Checkbutton(
                self.reminder_list, text=f"{reminder['date']} - {reminder['message']} - {status_text}",
                variable=reminder["status"], onvalue=1, offvalue=0,
                command=lambda i=i: self.update_status(i)
            )
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
    def __init__(self, window):
        self.window = window
        self.window.title("Dayminder")
        self.events = []
        self.add_event_button_visible = True

    def show_components(self):
        self.hide_add_event_button()

        # Add Event Manager components
        event_frame = tk.LabelFrame(self.window, text="Event Manager")
        event_frame.pack(padx=10, pady=10, fill="both", expand=True)

        event_listbox = tk.Listbox(event_frame, selectmode=tk.SINGLE)
        event_listbox.pack(padx=10, pady=10, fill="both", expand=True)
        event_listbox.bind('<<ListboxSelect>>', self.show_event_details)

        event_details_label = tk.Label(self.window, text="", wraplength=300)
        event_details_label.pack(padx=10, pady=5)

        add_event_button = tk.Button(self.window, text="Add Event", command=self.add_event)
        add_event_button.pack(padx=10, pady=5)

        self.update_event_listbox()

    def hide_add_event_button(self):
        if self.add_event_button_visible:
            for widget in self.window.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text") == "Add Event":
                    widget.pack_forget()
            self.add_event_button_visible = False

    def show_add_event_button(self):
        if not self.add_event_button_visible:
            for widget in self.window.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text") == "Add Event":
                    widget.pack()
            self.add_event_button_visible = True

    def add_event(self):
        # Hide the "Add Event" button
        self.hide_add_event_button()

        add_window = tk.Toplevel(self.window)
        add_window.title("Add Event")
        tk.Label(add_window, text="Event Title:").pack()
        event_title_entry = tk.Entry(add_window)
        event_title_entry.pack()
        tk.Label(add_window, text="Event Date:").pack()
        event_date_entry = DateEntry(add_window, width=12, background="darkblue", foreground="white", borderwidth=2)
        event_date_entry.pack()
        save_button = tk.Button(add_window, text="Save", command=lambda: self.save_event(event_title_entry.get(), event_date_entry.get(), add_window))
        save_button.pack()

    def save_event(self, title, date, window):
        if title and date:
            self.events.append({"title": title, "date": date})
            window.destroy()
            self.update_event_listbox()
            # Show the "Add Event" button again
            self.show_add_event_button()
        else:
            messagebox.showwarning("Warning", "Please enter event title and date.")

    def update_event_listbox(self):
        # Find the Listbox inside the LabelFrame
        event_listbox = next((widget for widget in self.window.winfo_children() if isinstance(widget, tk.Listbox)), None)

        if event_listbox:
            event_listbox.delete(0, tk.END)
            for event in self.events:
                event_listbox.insert(tk.END, f"{event['title']} - {event['date']}")

    def show_event_details(self, event):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.events[selected_index[0]]
            event_details = f"Title: {selected_event.get('title', '')}\n" \
                            f"Date: {selected_event.get('date', '')}"
            # Find the Label widget inside the main window
            event_details_label = next((widget for widget in self.window.winfo_children() if isinstance(widget, tk.Label)), None)
            if event_details_label:
                event_details_label.config(text=event_details)
        else:
            # Find the Label widget inside the main window
            event_details_label = next((widget for widget in self.window.winfo_children() if isinstance(widget, tk.Label)), None)
            if event_details_label:
                event_details_label.config(text="")


def main():
    window = tk.Tk()
    app = ReminderApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()
