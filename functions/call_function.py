from google.genai import types
from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

func_dict = {'get_file_content': get_file_content, 'get_files_info': get_files_info, 'run_python_file': run_python_file, 'write_file': write_file}

def call_function(function_call_part: types.FunctionCall, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    k_args = function_call_part.args
    k_args['working_directory'] = './calculator'

    
    if function_call_part.name in func_dict:
        function_result = func_dict[function_call_part.name](**k_args)
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": function_result},
        )
    ],
)
    else:
       return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
) 

