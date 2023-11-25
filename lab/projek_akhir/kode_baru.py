# kode shaula

import tkinter as tk
from tkinter import messagebox

class EventManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengingat Acara")

        # Buat dictionary untuk menyimpan data acara
        self.events = {}

        # Buat LabelFrame untuk menampilkan daftar acara
        self.event_frame = tk.LabelFrame(root, text="Daftar Acara")
        self.event_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Buat listbox untuk menampilkan daftar acara
        self.event_listbox = tk.Listbox(self.event_frame, width=50, height=15)
        self.event_listbox.pack(padx=10, pady=10, fill="both", expand=True)
        self.event_listbox.bind('<<ListboxSelect>>', self.show_event_details)  # Bind fungsi saat listbox dipilih

        # Buat label untuk menampilkan detail acara
        self.event_details_label = tk.Label(root, text="", wraplength=300)
        self.event_details_label.pack(padx=10, pady=5)

        # Buat tombol untuk menambah acara baru
        add_event_button = tk.Button(root, text="Tambah Acara", command=self.add_event)
        add_event_button.pack(padx=10, pady=5)

        # Panggil method untuk memperbarui listbox dengan acara yang ada
        self.update_event_listbox()

    def add_event(self):
        # Fungsi untuk menambah acara baru
        add_window = tk.Toplevel(self.root)
        add_window.title("Tambah Acara")

        # Buat label dan entry untuk input judul acara
        tk.Label(add_window, text="Judul Acara:").pack()
        event_title_entry = tk.Entry(add_window)
        event_title_entry.pack()

        # Buat label dan OptionMenu untuk input tanggal acara (dd-mm-yyyy)
        tk.Label(add_window, text="Tanggal:").pack()
        day_var = tk.StringVar(add_window)
        days = [str(day).zfill(2) for day in range(1, 32)]  # Menghasilkan angka 01-31
        day_var.set(days[0])
        day_dropdown = tk.OptionMenu(add_window, day_var, *days)
        day_dropdown.pack(side=tk.LEFT, padx=5)

        month_var = tk.StringVar(add_window)
        months = [str(month).zfill(2) for month in range(1, 13)]  # Menghasilkan angka 01-12
        month_var.set(months[0])
        month_dropdown = tk.OptionMenu(add_window, month_var, *months)
        month_dropdown.pack(side=tk.LEFT, padx=5)

        year_var = tk.StringVar(add_window)
        years = [str(year) for year in range(2020, 2051)]  # Menghasilkan tahun 2020-2050
        year_var.set(years[0])
        year_dropdown = tk.OptionMenu(add_window, year_var, *years)
        year_dropdown.pack(side=tk.LEFT, padx=5)

        # Buat checkbox untuk menandai apakah acara diprioritaskan atau tidak
        tk.Label(add_window, text="Prioritaskan Acara?").pack()
        event_priority_var = tk.IntVar()
        event_priority_checkbox = tk.Checkbutton(add_window, text="Ya", variable=event_priority_var)
        event_priority_checkbox.pack()

        # Buat tombol untuk menyimpan acara baru
        save_button = tk.Button(add_window, text="Simpan", command=lambda: self.save_event(
            event_title_entry.get(), day_var.get() + '-' + month_var.get() + '-' + year_var.get(),
            event_priority_var.get(), add_window))
        save_button.pack()

    def save_event(self, title, date, priority, window):
        # Fungsi untuk menyimpan acara baru ke dalam dictionary events
        if title and date:
            self.events[title] = {"Judul": title, "Tanggal": date, "Prioritas": priority}
            window.destroy()  # Tutup jendela setelah menyimpan acara
            self.update_event_listbox()
        else:
            messagebox.showwarning("Peringatan", "Mohon isi judul dan tanggal acara.")

    def update_event_listbox(self):
        # Fungsi untuk memperbarui listbox dengan daftar acara
        self.event_listbox.delete(0, tk.END)  # Hapus isi listbox saat ini
        for event in self.events:
            self.event_listbox.insert(tk.END, self.events[event]["Judul"])

    def show_event_details(self, event):
        # Fungsi untuk menampilkan detail acara saat dipilih
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_title = self.event_listbox.get(selected_index[0])
            details = self.events.get(selected_title, {})
            event_details = f"Judul: {details.get('Judul', '')}\n" \
                            f"Tanggal: {details.get('Tanggal', '')}\n" \
                            f"Prioritas: {'Ya' if details.get('Prioritas', 0) else 'Tidak'}"
            self.event_details_label.config(text=event_details)
        else:
            self.event_details_label.config(text="")

def main():
    root = tk.Tk()
    app = EventManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
