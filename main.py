import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tests import *
import sys

def main():
    load_dotenv()
    get_files_info()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("Prompt missing")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    
    if len(sys.argv) == 3:
        if str(sys.argv[2]) == "--verbose":
            print(f"User prompt: {user_prompt}")
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

    print(response.text)


if __name__ == "__main__":
    main()
