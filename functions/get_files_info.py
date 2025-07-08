import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_directory = os.path.join(absolute_working_directory, directory)
    print("this is the absolute_directory", absolute_directory)

    if not absolute_directory.startswith(absolute_working_directory) or directory == "../":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_directory):
        return f'Error: "{directory}" is not a directory'
    try:
        dirs = os.listdir(absolute_directory)
        list_of_dirs = []
        for file in dirs:
            absolute_file_path = os.path.join(absolute_directory, file)
            file_size = os.path.getsize(absolute_file_path)
            is_dir = os.path.isdir(absolute_file_path)
            list_of_dirs.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(list_of_dirs)
    except Exception as e:
        return f"Error listing files: {e}"
  
       
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    