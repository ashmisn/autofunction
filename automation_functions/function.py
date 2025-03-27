import os
import webbrowser
import psutil
import subprocess

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc" if os.name == "nt" else "gnome-calculator")

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def execute_command(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout
