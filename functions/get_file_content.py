import os


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