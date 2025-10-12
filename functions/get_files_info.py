import os

def get_files_info(working_directory, directory='.'):
    relative_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(relative_path)
    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permittedworking directory\n'
    elif not os.path.isdir(relative_path):
        return f'Error: "{directory}" is not a directory\n'
    try:
        output = ''
        for path in os.listdir(relative_path):
            output += f'- {path}: file_size={os.path.getsize(os.path.join(relative_path, path))} bytes, is_dir={os.path.isdir(os.path.join(relative_path, path))}\n'
    except Exception as e:
        return 'Error: ' + str(e) 
    return output
