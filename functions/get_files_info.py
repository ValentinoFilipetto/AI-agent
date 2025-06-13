import os

# We're returning strings here because we want get_files_info to always return a string that the LLM can read.
# This way, when it encounters an error, it can try again with a different approach.
def get_files_info(working_directory, directory=None):
    if not directory:
        directory = "."

    directory_to_check = os.path.normpath(os.path.join(os.path.abspath(working_directory), directory))

    if not directory_to_check.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_to_check):
        return f'Error: "{directory}" is not a directory'

    try:
        res = ""
        for element in os.listdir(directory_to_check):
            element_to_check = os.path.join(os.path.abspath(directory_to_check), element)
            is_file = os.path.isfile(element_to_check)
            is_dir = os.path.isdir(element_to_check)

            if is_file:
                res += f"{element}: file_size={os.path.getsize(element_to_check)}, is_dir={is_dir}\n"
            elif is_dir:
                res += f"{element}: file_size={os.path.getsize(element_to_check)}, is_dir={is_dir}\n"

    except Exception as e:
        return f"Error: {e}"

    return res

def get_file_content(working_directory, file_path):
    file_to_check = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_to_check.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_to_check):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(file_to_check, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):  # Try to read one more character to check if file is longer
                file_content_string = file_content_string.rstrip('\n') + f'\n...File "{file_path}" truncated at 10000 characters'
    except Exception as e:
        return f"Error: {e}"

    return file_content_string
