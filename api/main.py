from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from vector_store.store import retrieve_function


app = FastAPI()

class UserInput(BaseModel):
    prompt: str  # User's natural language input

# Define function implementations
function_map = {
    "open_chrome": lambda: subprocess.run(["start", "chrome"], shell=True),
    "open_calculator": lambda: subprocess.run("calc.exe", shell=True),
    "get_cpu_usage": lambda: subprocess.run(["wmic", "cpu", "get", "loadpercentage"], shell=True),
}

@app.post("/execute")
def execute_function(user_input: UserInput):
    function_name = retrieve_function(user_input.prompt)  # Retrieve best match
    if function_name and function_name in function_map:
        function_map[function_name]()  # Run function
        return {"status": "success", "executed_function": function_name}
    return {"status": "error", "message": "No matching function found"}
