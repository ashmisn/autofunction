# Automation API

## Overview
This project is an automation API that maps user commands to specific functions using FAISS for similarity matching. The API is built with FastAPI and utilizes sentence embeddings to determine the closest function based on user input.

## Features
- Uses FAISS for fast and efficient similarity search
- Supports various automation tasks like opening applications and fetching system info
- REST API interface using FastAPI
- Works with sentence embeddings for command recognition

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ashmisn/autofunction.git
cd autofunction
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the API

### Start the FastAPI Server
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
After running the above command, the API will be available at `http://127.0.0.1:8000`.

## Using the API

### Making Requests via PowerShell
#### Sending a command request
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/execute" -Method Post -Body '{"prompt": "want to calculate"}' -ContentType "application/json"
```

#### Alternative (Better for JSON Parsing)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/execute" -Method Post -Body '{"prompt": "open calculator"}' -ContentType "application/json"
```

## API Endpoints

### `POST /execute`
Executes a command based on the closest matching function.

**Request Body:**
```json
{
  "prompt": "open calculator"
}
```

**Response:**
```json
{
  "matched_function": "open_calculator"
}
```

## Troubleshooting
- **If the module `main` is not found**, ensure you are inside the correct directory (`api`) before running Uvicorn.
- **If the PowerShell command gives an error**, try `Invoke-RestMethod` instead of `Invoke-WebRequest`.

## License
This project is open-source and available under the MIT License.

---
Feel free to contribute to the project by submitting pull requests!



