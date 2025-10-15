import os

def write_file(working_directory, file_path, content):
    relative_path = os.path.join(working_directory, file_path)
    abs_work_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(relative_path)
    if not abs_file_path.startswith(abs_work_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Overwrite all contents of file with file path if it exists
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f'Error: {e}')
