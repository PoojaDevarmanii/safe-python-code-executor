Safe Code Executor

This project provides a simple and safe API for executing Python code inside Docker containers. It is designed as a learning project to understand how to run untrusted code securely and how to apply Docker-based sandboxing.

Features

Execute Python code inside a Docker container
Network access disabled for executed code
Temporary file-based execution
Automatic cleanup of temporary files
Simple web-based UI for running code
Flask backend with a /run API endpoint
Support for basic Docker isolation

Project Structure
safe-code-executor/
│   app.py
│   executor.py
│   README.md
│
├── static
│     index.html
│
└── tests
      infinite_loop.py
      memory_attack.py
      network_attack.py

Requirements

Python 3.10+
Docker installed and running
Flask installed via requirements.txt
Install dependencies:
pip install -r requirements.txt

How to Run the Project

Navigate to the project directory:
cd "C:\Users\pooja\OneDrive\Desktop\docker learn\safe-code-executor"
Start the Flask server:
python app.py
Open the web UI:
http://127.0.0.1:5000/
This loads the index.html file from the static folder.

API Usage
Endpoint
POST /run

Request Body Example
{
  "code": "print(2 + 2)"
}

Response Example
{
  "output": "4"
}

Security Measures Implemented
Docker containerization for code execution
Read-only root filesystem for containers
No network access (--network none)
Automatic cleanup of temporary Python files
Isolation of executed code from the host system
timeout commands can be added for infinite loop protection
Code execution performed using separate container processes
Understanding Docker Security

The project allows you to experiment with:

Accessing files inside the container
Example: reading /etc/passwd.

Writing files inside the container
Possible unless filesystem is mounted read-only.

Testing network access
Should fail due to --network none.

Testing memory usage and infinite loops
Can be limited using Docker flags.

These tests help understand the limits and capabilities of Docker-based isolation.
Tests Included
The tests folder contains:

infinite_loop.py
For testing execution timeout behavior.

memory_attack.py
For testing memory restrictions.

network_attack.py
For testing network isolation.

What we Learn from This Project

How to execute untrusted code safely
How to integrate Docker with a Flask API
How to limit system access using Docker options
How code sandboxes work
How to design a simple web-based interface for code execution
Future Improvements
Add CPU and memory limits to the Docker run command
Add execution timeout handling
Add support for additional programming languages
Add container non-root execution
Add a history page for previous executions
Implement a more advanced security model using seccomp profiles