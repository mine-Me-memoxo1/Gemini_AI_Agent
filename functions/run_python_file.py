import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        relative_path = os.path.join(working_directory, file_path)
        abs_path = os.path.abspath(relative_path)
        abs_working_path = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        elif not os.path.exists(abs_path):
            return f'Error: File "{file_path}" not found.'

        elif not file_path.endswith('.py'):
            return f'Error: File "{file_path}" is not a Python file.'

        completed_process = subprocess.run(['python3', f'{abs_path}'] + args, capture_output=True,timeout=30, cwd = abs_working_path,text=True)

        outstring = f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n'

        if completed_process.returncode:
            outstring += 'Process exited with code {completed_process.returncode}'          
        if not outstring:
            return 'No output produced'
        else:
            return outstring

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
                    

