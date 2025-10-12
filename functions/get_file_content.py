import os
from config import MAX_CHARS
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

