# AI-agent

## Project idea

This is an AI agent similar to [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) or [Aider](https://aider.chat/). This agent:

- Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽")
- Chooses from a set of predefined functions to work on the task, for example:
  - Scan the files in a directory
  - Read a file's contents
  - Overwrite a file's contents
  - Execute the python interpreter on a file
- Repeats step 2 until the task is complete (or it fails miserably, which is possible)

## Prerequisites

- Python 3.10+ installed
- Access to a Unix-like shell (e.g. zsh or bash)

## How to run this agent on your local machine

- Clone the repository
- Create a virtual environment at the top level of your project directory:

```bash
python3 -m venv venv
```

- Activate the virtual environment:

  - On Mac/Linux

    ```bash
    source venv/bin/activate
    ```

  - On Windows

    ```bash
    source venv/Scripts/activate
    ```

- Create an accout on [Google AI Studio](https://aistudio.google.com/prompts/new_chat) if you don't already have one
- Click the "Create API Key" button.
- Copy the API key, then paste it into a new `.env` file in your project directory. The file should look like this:

```.env
GEMINI_API_KEY="your_api_key_here"
```

- Run the code:

```bash
python3 main.py
```
