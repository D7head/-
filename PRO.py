import tkinter as tk
import random
import pyautogui
import os
import time
from PIL import ImageGrab

def flicker():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    while True:
        color = random.choice(colors)
        root.configure(bg=color)
        root.update()
        time.sleep(0.1)

def show_errors():
    messages = [
        "Critical Error: System Failure",
        "Memory Corruption Detected",
        "File System Error",
        "Access Violation",
        "Runtime Error"
    ]
    while True:
        message = random.choice(messages)
        pyautogui.alert(message, "ERROR")
        time.sleep(random.uniform(1, 5))
y
def erratic_mouse():
    screen_width, screen_height = pyautogui.size()
    while True:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.dragTo(random.randint(0, screen_width), random.randint(0, screen_height), duration=0.2, button='left')
        time.sleep(0.1)

def manipulate_desktop():
    while True:
        screenshot = ImageGrab.grab()
        screenshot = screenshot.convert("L")  
        screenshot.save("desktop_glitch.png")
        os.system("attrib +h desktop_glitch.png") 
        time.sleep(5)

import threading

threading.Thread(target=flicker).start()
threading.Thread(target=show_errors).start()
threading.Thread(target=erratic_mouse).start()
threading.Thread(target=manipulate_desktop).start()
