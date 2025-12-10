import os
import tempfile
import subprocess

def run_python_safely(code):
    # Create temporary script file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    try:
        cmd = [
            "docker", "run", "--rm",
            
            "--memory=128m",           # memory limit
            "--cpus=0.5",              # CPU limit
            "--network", "none",       # disable network
            "--read-only",             # prevent writing to FS

            "-v", f"{tmp_path}:/code.py:ro",

            "python:3.11-slim",

            "timeout", "10",           # kill infinite loop
            "python", "/code.py"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Timeout
        if result.returncode == 124:
            return "Execution timed out after 10 seconds"

        output = result.stdout + result.stderr
        return output.strip()

    finally:
        os.remove(tmp_path)
