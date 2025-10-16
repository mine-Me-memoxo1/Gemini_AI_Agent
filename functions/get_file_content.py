import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        relative_path = os.path.join(working_directory, file_path)
        abs_file_path = os.path.abspath(relative_path)
        working_abs_path = os.path.abspath(working_directory)
        if not abs_file_path.startswith(working_abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path) as f:
            out = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) >= MAX_CHARS:
                out += '\n[...File "{}" truncated at {} characters]\n'.format(file_path, MAX_CHARS)
            return out
    
    except Exception as e:
        return f'Error: {e}'


schema_get_file_content = types.FunctionDeclaration(
        name='get_file_content',
        description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                'file_path': types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file whose content should be read, relative to the working directory."
                    )
                }
            )
        )
