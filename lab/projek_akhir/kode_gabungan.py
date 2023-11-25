import tkinter as tk
from tkinter import messagebox, IntVar
from tkcalendar import DateEntry
from datetime import datetime
from ttkthemes import ThemedStyle

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder and Event Manager")
        self.root.minsize(width=500, height=400)

        # Reminder App components
        self.setup_reminder_app()

        # Event Manager components
        self.event_manager = EventManager(root)

    def setup_reminder_app(self):
        # Calendar widget
        self.cal = DateEntry(self.root, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.cal.pack(pady=20)

        # Entry for reminder message
        self.message_entry = tk.Entry(self.root, width=30)
        self.message_entry.pack(pady=10)

        # Button to set reminder
        reminder_button = tk.Button(self.root, text="Set Reminder", command=self.set_reminder)
        reminder_button.pack(pady=10)

        # Reminder data list
        self.reminders = []  # Each reminder is now a dictionary with 'date', 'message', and 'status'

        # Show reminders button
        show_reminders_button = tk.Button(self.root, text="Show Reminders", command=self.show_reminders)
        show_reminders_button.pack(pady=5)

        # Reminder listbox
        self.reminder_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.reminder_list.pack(pady=10)

        # Delete selected reminder button
        delete_button = tk.Button(self.root, text="Delete Selected Reminder", command=self.delete_selected_reminder)
        delete_button.pack(pady=5)

        # Show notification button
        show_notification_button = tk.Button(self.root, text="Show Notification", command=self.show_notification)
        show_notification_button.pack(pady=5)

    def set_reminder(self):
        date_selected = self.cal.get_date()
        reminder_date = datetime.strptime(date_selected.strftime("%m/%d/%y"), "%m/%d/%y").date()
        current_date = datetime.now().date()

        if reminder_date >= current_date:
            formatted_date = date_selected.strftime("%m/%d/%y")
            message = self.message_entry.get()  # Get the message from the entry
            status = IntVar()
            self.reminders.append({"date": formatted_date, "message": message, "status": status})
            messagebox.showinfo("Reminder Set", f"Reminder set for {formatted_date} with message: {message}")
            self.show_reminders()
        else:
            messagebox.showerror("Invalid Date", "Please select a valid date.")

    def show_reminders(self):
        self.reminder_list.delete(0, tk.END)
        for reminder in self.reminders:
            status_text = "Done" if reminder["status"].get() else "Not Done"
            self.reminder_list.insert(tk.END, f"{reminder['date']} - {reminder['message']} - {status_text}")

    def delete_selected_reminder(self):
        selected_index = self.reminder_list.curselection()
        if selected_index:
            self.reminders.pop(selected_index[0])
            self.show_reminders()

    def show_notification(self):
        selected_index = self.reminder_list.curselection()
        if selected_index:
            selected_reminder = self.reminders[selected_index[0]]
            status_text = "Done" if selected_reminder["status"].get() else "Not Done"
            messagebox.showinfo("Reminder", f"{selected_reminder['message']} - {selected_reminder['date']} - {status_text}")

class EventManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Manager")

        # Your existing EventManager implementation remains here...

def main():
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
