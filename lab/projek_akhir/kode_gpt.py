# # WEATHER APP

# import tkinter as tk
# from tkinter import messagebox
# import requests

# def get_weather(city):
#     api_key = "bb36f687e3df1168ca3299a08eb7fcb1"  # Ganti dengan kunci API OpenWeatherMap Anda
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key, "units": "metric"}

#     try:
#         response = requests.get(base_url, params=params)
#         weather_data = response.json()
#         temperature = weather_data["main"]["temp"]
#         description = weather_data["weather"][0]["description"]
#         result = f"Temperature: {temperature}°C\nDescription: {description}"
#         return result
#     except Exception as e:
#         return str(e)

# def get_weather_report():
#     city = city_entry.get()
#     if city:
#         weather_report = get_weather(city)
#         result_label.config(text=weather_report)
#     else:
#         messagebox.showwarning("Warning", "Please enter a city.")

# # GUI setup
# app = tk.Tk()
# app.title("Weather App")

# # Widgets
# label = tk.Label(app, text="Enter City:")
# label.pack(pady=10)

# city_entry = tk.Entry(app)
# city_entry.pack(pady=10)

# get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_report)
# get_weather_button.pack(pady=10)

# result_label = tk.Label(app, text="")
# result_label.pack(pady=10)

# # Run the application
# app.mainloop()


# # TO-DO LIST
# import tkinter as tk
# from tkinter import messagebox

# def add_task():
#     task = entry.get()
#     if task:
#         listbox.insert(tk.END, task)
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Warning", "Please enter a task.")

# def delete_task():
#     try:
#         selected_task_index = listbox.curselection()[0]
#         listbox.delete(selected_task_index)
#     except IndexError:
#         messagebox.showwarning("Warning", "Please select a task to delete.")

# # GUI setup
# app = tk.Tk()
# app.title("To-Do List App")

# # Widgets
# entry = tk.Entry(app, width=30)
# entry.pack(pady=10)

# add_button = tk.Button(app, text="Add Task", command=add_task)
# add_button.pack(pady=5)

# delete_button = tk.Button(app, text="Delete Task", command=delete_task)
# delete_button.pack(pady=5)

# listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
# listbox.pack(pady=10)

# # Run the application
# app.mainloop()


# # MUSIC PLAYER PYGAME
# import tkinter as tk
# from tkinter import filedialog
# import pygame

# def play_music():
#     try:
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#         status_label.config(text="Now Playing: " + file_path)
#     except Exception as e:
#         status_label.config(text="Error: " + str(e))

# def stop_music():
#     pygame.mixer.music.stop()
#     status_label.config(text="Music Stopped")

# def choose_file():
#     global file_path
#     file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
#     if file_path:
#         status_label.config(text="Selected File: " + file_path)

# # Initialize Pygame
# pygame.mixer.init()

# # GUI setup
# app = tk.Tk()
# app.title("Music Player")

# # Widgets
# choose_file_button = tk.Button(app, text="Choose Music File", command=choose_file)
# choose_file_button.pack(pady=10)

# play_button = tk.Button(app, text="Play", command=play_music)
# play_button.pack(pady=5)

# stop_button = tk.Button(app, text="Stop", command=stop_music)
# stop_button.pack(pady=5)

# status_label = tk.Label(app, text="Status: No music selected")
# status_label.pack(pady=10)

# # Run the application
# app.mainloop()


# # MUSIC PLAYER THREADING
# import os
# import tkinter as tk
# from tkinter import filedialog
# import threading
# import time
# import subprocess
# import ctypes as ct


# def dark_title_bar(window):
#     """
#     MORE INFO:
#     https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
#     """
#     window.update()
#     DWMWA_USE_IMMERSIVE_DARK_MODE = 20
#     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
#     get_parent = ct.windll.user32.GetParent
#     hwnd = get_parent(window.winfo_id())
#     rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
#     value = 2
#     value = ct.c_int(value)
#     set_window_attribute(hwnd, rendering_policy, ct.byref(value),
#                          ct.sizeof(value))

# def play_music():
#     global playing
#     try:
#         subprocess.Popen(['start', '', file_path], shell=True)
#         status_label.config(text=f"Now Playing: {file_name}", bg='#2C2A2C', fg='#FFF')
#         playing = True
#     except Exception as e:
#         status_label.config(text="Error: " + str(e), bg='#2C2A2C', fg='#FFF')

# def stop_music():
#     global playing
#     try:
#         subprocess.run(["taskkill", "/F", "/IM", 'Microsoft.Media.Player.exe'], shell=True)
#         status_label.config(text="Music Stopped", bg='#2C2A2C', fg='#FFF')
#         playing = False
#     except Exception as e:
#         status_label.config(text="Error: " + str(e), bg='#2C2A2C', fg='#FFF')

# def choose_file():
#     global file_path, file_name
#     file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
#     if file_path:
#         file_name = os.path.basename(file_path)
#         status_label.config(text="Selected File: " + file_name, bg='#2C2A2C', fg='#FFF')


# def update_status():
#     global playing
#     while playing:
#         time.sleep(1)
#     status_label.config(text="Music Stopped", bg='#2C2A2C', fg='#FFF')

# # Global variables
# playing = False
# file_path = ""
# file_name = None

# # GUI setup
# app = tk.Tk()
# app.title("Music Player")
# app.minsize(width=400, height=100)
# app.config(background='#2C2A2C')
# dark_title_bar(app)

# # Widgets
# choose_file_button = tk.Button(app, text="Choose Music File", command=choose_file, bg='#8E6360', fg='#EFF0EF')
# choose_file_button.pack(pady=10)

# play_button = tk.Button(app, text="Play", command=play_music, bg='#8E6360', fg='#EFF0EF')
# play_button.pack(pady=5)

# stop_button = tk.Button(app, text="Stop", command=stop_music, bg='#8E6360', fg='#EFF0EF')
# stop_button.pack(pady=5)

# status_label = tk.Label(app, text="Status: No music selected", bg='#2C2A2C', fg='#FFF')
# status_label.pack(pady=10)

# # Run the application
# app.mainloop()

# # Start thread to update status
# status_thread = threading.Thread(target=update_status)
# status_thread.start()


# MUSIC PLAYER PYGAME FAILED
# import os
# import tkinter as tk
# from tkinter import filedialog
# import threading
# import time
# import subprocess
# import ctypes as ct
# import pygame

# pygame.init()


# def dark_title_bar(window):
#     """
#     MORE INFO:
#     https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
#     """
#     window.update()
#     DWMWA_USE_IMMERSIVE_DARK_MODE = 20
#     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
#     get_parent = ct.windll.user32.GetParent
#     hwnd = get_parent(window.winfo_id())
#     rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
#     value = 2
#     value = ct.c_int(value)
#     set_window_attribute(hwnd, rendering_policy, ct.byref(value),
#                          ct.sizeof(value))

# def play_music():
#     global playing, file_path, file_name

#     try:
#         pygame.mixer.init()
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#         status_label.config(text=f"Now Playing: {file_name}", bg='#2C2A2C', fg='#FFF')
#         playing = True
#     except Exception as e:
#         status_label.config(text="Error: " + str(e), bg='#2C2A2C', fg='#FFF')

# def stop_music():
#     global playing
#     try:
#         subprocess.run(["taskkill", "/F", "/IM", 'Microsoft.Media.Player.exe'], shell=True)
#         status_label.config(text="Music Stopped", bg='#2C2A2C', fg='#FFF')
#         playing = False
#     except Exception as e:
#         status_label.config(text="Error: " + str(e), bg='#2C2A2C', fg='#FFF')

# def choose_file():
#     global file_path, file_name
#     file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
#     if file_path:
#         file_name = os.path.basename(file_path)
#         status_label.config(text="Selected File: " + file_name, bg='#2C2A2C', fg='#FFF')


# def update_status():
#     global playing
#     while playing:
#         time.sleep(1)
#     status_label.config(text="Music Stopped", bg='#2C2A2C', fg='#FFF')

# # Global variables
# playing = False
# file_path = ""
# file_name = None

# # GUI setup
# app = tk.Tk()
# app.title("Music Player")
# app.minsize(width=400, height=100)
# app.config(background='#2C2A2C')
# dark_title_bar(app)

# # Widgets
# choose_file_button = tk.Button(app, text="Choose Music File", command=choose_file, bg='#8E6360', fg='#EFF0EF')
# choose_file_button.pack(pady=10)

# play_button = tk.Button(app, text="Play", command=play_music, bg='#8E6360', fg='#EFF0EF')
# play_button.pack(pady=5)

# stop_button = tk.Button(app, text="Stop", command=stop_music, bg='#8E6360', fg='#EFF0EF')
# stop_button.pack(pady=5)

# status_label = tk.Label(app, text="Status: No music selected", bg='#2C2A2C', fg='#FFF')
# status_label.pack(pady=10)

# # Run the application
# app.mainloop()

# # Start thread to update status
# status_thread = threading.Thread(target=update_status)
# status_thread.start()


# Simple Calculator

# import tkinter as tk

# def on_button_click(value):
#     current_text = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current_text + str(value))

# def clear_entry():
#     entry.delete(0, tk.END)

# def calculate_result():
#     try:
#         expression = entry.get()
#         result = eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # GUI setup
# app = tk.Tk()
# app.title("Simple Calculator")

# # Entry widget for input and display
# entry = tk.Entry(app, width=20, font=('Arial', 14))
# entry.grid(row=0, column=0, columnspan=4)

# # Buttons
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]

# row_val = 1
# col_val = 0

# for button in buttons:
#     tk.Button(app, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# # Clear button
# tk.Button(app, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)

# # Equal button
# tk.Button(app, text="=", width=5, height=2, command=calculate_result).grid(row=row_val, column=col_val + 1)

# # Run the application
# app.mainloop()


# Money Converter

# import tkinter as tk
# from tkinter import ttk
# import requests

# class CurrencyConverter:
#     def __init__(self, app):
#         self.app = app
#         self.app.title("Currency Converter")

#         self.amount_label = ttk.Label(app, text="Enter Amount:")
#         self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

#         self.amount_entry = ttk.Entry(app, width=15, font=('Arial', 14))
#         self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

#         self.from_currency_label = ttk.Label(app, text="From Currency:")
#         self.from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

#         self.from_currency_combobox = ttk.Combobox(app, values=self.get_currency_list(), width=15)
#         self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
#         self.from_currency_combobox.set("USD")

#         self.to_currency_label = ttk.Label(app, text="To Currency:")
#         self.to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

#         self.to_currency_combobox = ttk.Combobox(app, values=self.get_currency_list(), width=15)
#         self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
#         self.to_currency_combobox.set("EUR")

#         self.convert_button = ttk.Button(app, text="Convert", command=self.convert_currency)
#         self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

#         self.result_label = ttk.Label(app, text="")
#         self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

#     def get_currency_list(self):
#         # Get the list of currencies from the API
#         url = "https://open.er-api.com/v6/latest"
#         response = requests.get(url)
#         data = response.json()
#         currencies = list(data["rates"].keys())
#         return currencies

#     def convert_currency(self):
#         try:
#             amount = float(self.amount_entry.get())
#             from_currency = self.from_currency_combobox.get()
#             to_currency = self.to_currency_combobox.get()

#             # Get the exchange rate from the API
#             url = f"https://open.er-api.com/v6/latest?base={from_currency}"
#             response = requests.get(url)
#             data = response.json()
#             exchange_rate = data["rates"][to_currency]

#             # Perform the conversion
#             result = amount * exchange_rate
#             formatted_amount = "{:,.2f}".format(amount)
#             formatted_result = "{:,.2f}".format(result)
#             self.result_label.config(text=f"Result: {formatted_amount} {from_currency} = {formatted_result} {to_currency}")
#         except Exception as e:
#             self.result_label.config(text="Error: Invalid input or conversion failed")

# if __name__ == "__main__":
#     app = tk.Tk()
#     converter = CurrencyConverter(app)
#     app.mainloop()


# Health Note App

# import tkinter as tk
# from tkinter import ttk

# class HealthNotesApp:
#     def __init__(self, app):
#         self.app = app
#         self.app.title("Health Notes App")

#         self.weight_label = ttk.Label(app, text="Weight (kg):")
#         self.weight_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

#         self.weight_entry = ttk.Entry(app, width=15, font=('Arial', 14))
#         self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

#         self.blood_pressure_label = ttk.Label(app, text="Blood Pressure:")
#         self.blood_pressure_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

#         self.blood_pressure_entry = ttk.Entry(app, width=15, font=('Arial', 14))
#         self.blood_pressure_entry.grid(row=1, column=1, padx=10, pady=10)

#         self.height_label = ttk.Label(app, text="Height (cm):")
#         self.height_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

#         self.height_entry = ttk.Entry(app, width=15, font=('Arial', 14))
#         self.height_entry.grid(row=2, column=1, padx=10, pady=10)

#         self.save_button = ttk.Button(app, text="Save", command=self.save_health_data)
#         self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

#         self.result_label = ttk.Label(app, text="")
#         self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

#     def save_health_data(self):
#         try:
#             weight = float(self.weight_entry.get())
#             blood_pressure = self.blood_pressure_entry.get()
#             height = float(self.height_entry.get())

#             # Save health data to a file or database as needed
#             # Here, we print the data as an example
#             result_text = f"Weight: {weight} kg\nBlood Pressure: {blood_pressure}\nHeight: {height} cm"
#             self.result_label.config(text=result_text)
#         except Exception as e:
#             self.result_label.config(text="Error: Invalid input")

# if __name__ == "__main__":
#     app = tk.Tk()
#     health_notes_app = HealthNotesApp(app)
#     app.mainloop()


# Simple Quiz

import tkinter as tk
from tkinter import ttk
import random

class SimpleQuizApp:
    def __init__(self, app):
        self.app = app
        self.app.title("Simple Quiz App")

        self.question_label = ttk.Label(app, text="Question:")
        self.question_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.question_text = ttk.Label(app, text="")
        self.question_text.grid(row=0, column=1, padx=10, pady=10)

        self.answer_label = ttk.Label(app, text="Your Answer:")
        self.answer_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.answer_entry = ttk.Entry(app, width=20, font=('Arial', 14))
        self.answer_entry.grid(row=1, column=1, padx=10, pady=10)

        self.check_button = ttk.Button(app, text="Check Answer", command=self.check_answer)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(app, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.score_label = ttk.Label(app, text="Score: 0")
        self.score_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Quiz data (change or add questions as needed)
        self.quiz_data = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        ]

        # Initialize the quiz
        self.current_question = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        # Load the current question
        question_data = self.quiz_data[self.current_question]
        self.question_text.config(text=question_data["question"])
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def check_answer(self):
        # Check the answer and provide feedback
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.quiz_data[self.current_question]["answer"].lower()

        if user_answer == correct_answer:
            self.result_label.config(text="Correct!", foreground="green")
            self.score += 1
        else:
            self.result_label.config(text="Incorrect. The correct answer is: " + correct_answer, foreground="red")

        # Move to the next question or end the quiz
        self.current_question += 1
        if self.current_question < len(self.quiz_data):
            self.load_question()
        else:
            self.result_label.config(text="Quiz completed! Your final score is: " + str(self.score))
            self.check_button.config(state=tk.DISABLED)  # Disable the Check Answer button
            self.score_label.config(text="Final Score: " + str(self.score))

if __name__ == "__main__":
    app = tk.Tk()
    quiz_app = SimpleQuizApp(app)
    app.mainloop()

