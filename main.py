import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from function_schemas import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
)
from functions.call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    system_prompt = """
                    You are a helpful AI coding agent.
                    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
                    - List files and directories
                    - Read file contents
                    - Execute Python files with optional arguments
                    - Write or overwrite files
                    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                    """

    ## these are the arguments that a user typed
    script_args = sys.argv

    if len(script_args) < 2:
        print("not enough arguments provided to script")
        exit(1)

    client = genai.Client(api_key=api_key)
    user_prompt = script_args[1]

    ## create a "user" role in the conversation
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        ## Show tokens used if "--verbose" flag is enabled
        if len(script_args) == 3 and script_args[2] == "--verbose":
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(
                    function_call_part,
                    verbose=(len(script_args) == 3 and script_args[2] == "--verbose"),
                )

                ## LLM needs to be aware of function responses
                messages.append(function_call_result)

        ## we return when LLM has no more functions to invoke
        else:
            print("---------------------------------------")
            print("Final response:\n")
            print(response.text)
            break


if __name__ == "__main__":
    main()
