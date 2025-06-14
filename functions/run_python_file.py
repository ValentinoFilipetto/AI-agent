import os
import subprocess


def run_python_file(working_directory, file_path):
    file_to_check = os.path.abspath(os.path.join(working_directory, file_path))
    # print(file_path, file_to_check)

    if not file_to_check.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_to_check):
        return f'Error: File "{file_path}" not found.'

    if not file_to_check.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", file_to_check],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            cwd=working_directory
        )

        stdout = result.stdout.decode('utf-8')
        stderr = result.stderr.decode('utf-8')
        output = []

        if not stdout and not stderr:
            return "No output produced."
        if stdout.strip():
            output.append(f"STDOUT:\n{stdout.strip()}")
        if stderr.strip():
            output.append(f"STDERR:\n{stderr.strip()}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"