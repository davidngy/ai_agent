import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.join(absolute_working_directory, file_path)
   
    if not absolute_file_path.startswith(absolute_working_directory) or "../" in file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    file = absolute_file_path.split("/")[-1]
    file_ending = file.split(".")[-1]

    if not file_ending == "py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        command = ["python3", file]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=absolute_working_directory
        )

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        
        if result.stderr:
                return f"STDERR:\n{result.stderr}"
        
        if result.stdout == "":
            return f"No output produced."

        
        return f"STDOUT:\n{result.stdout}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)