import os


def write_file(working_directory, file_path, content):
    file_to_check = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_to_check.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    # if the file does not exist, we create it
    if not os.path.isfile(file_to_check):
        try:
            os.makedirs(os.path.dirname(file_to_check), exist_ok=True)
        except Exception as e:
            return f"Error: {e}"

    try:
        ## write content on file
        with open(file_to_check, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
