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
import os
import tkinter as tk
from tkinter import filedialog
import threading
import time
import subprocess
import ctypes as ct


def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))

def play_music():
    global playing
    try:
        subprocess.Popen(['start', '', file_path], shell=True)
        status_label.config(text=f"Now Playing: {file_name}", bg='#EFF0EF')
        playing = True
    except Exception as e:
        status_label.config(text="Error: " + str(e))

def stop_music():
    global playing
    try:
        subprocess.run(["taskkill", "/F", "/IM", 'Microsoft.Media.Player.exe'], shell=True)
        status_label.config(text="Music Stopped")
        playing = False
    except Exception as e:
        status_label.config(text="Error: " + str(e))

def choose_file():
    global file_path, file_name
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        file_name = os.path.basename(file_path)
        status_label.config(text="Selected File: " + file_name)


def update_status():
    global playing
    while playing:
        time.sleep(1)
    status_label.config(text="Music Stopped")

# Global variables
playing = False
file_path = ""
file_name = None

# GUI setup
app = tk.Tk()
app.title("Music Player")
app.minsize(width=400, height=100)
app.config(background='#2C2A2C')
dark_title_bar(app)

# Widgets
choose_file_button = tk.Button(app, text="Choose Music File", command=choose_file, bg='#8E6360', fg='#EFF0EF')
choose_file_button.pack(pady=10)

play_button = tk.Button(app, text="Play", command=play_music, bg='#8E6360', fg='#EFF0EF')
play_button.pack(pady=5)

stop_button = tk.Button(app, text="Stop", command=stop_music, bg='#8E6360', fg='#EFF0EF')
stop_button.pack(pady=5)

status_label = tk.Label(app, text="Status: No music selected", bg='#8E6360', fg='#EFF0EF')
status_label.pack(pady=10)

# Run the application
app.mainloop()

# Start thread to update status
status_thread = threading.Thread(target=update_status)
status_thread.start()

