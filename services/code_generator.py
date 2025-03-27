import subprocess

# Define automation functions
def open_chrome():
    subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def open_calculator():
    subprocess.Popen("calc.exe")

def get_cpu_usage():
    import psutil
    return {"cpu_usage": psutil.cpu_percent(interval=1)}

def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {"output": result.stdout, "error": result.stderr}

# Map function names to actual functions
FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "get_cpu_usage": get_cpu_usage,
    "execute_command": execute_command
}

def generate_code(function_name):
    if function_name in FUNCTIONS:
        return FUNCTIONS[function_name]
    raise KeyError(f"Function '{function_name}' not found")
