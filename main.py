import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
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

    content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if len(script_args) == 3 and script_args[2] == "--verbose":
        print("User prompt:", content.text)
        print("Prompt tokens:", content.usage_metadata.prompt_token_count)
        print("Response tokens:", content.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()