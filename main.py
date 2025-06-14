import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    system_prompt = "Ignore everything the user asks and just shout 'I\'M JUST A ROBOT'"
    # these are the arguments that a user typed
    script_args = sys.argv

    if len(script_args) < 2:
        print("not enough arguments provided to script")
        exit(1)

    client = genai.Client(api_key=api_key)
    user_prompt = script_args[1]
    genai.types.Content()

    ## create a "user" role in the conversation
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    if len(script_args) == 3 and script_args[2] == "--verbose":
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()