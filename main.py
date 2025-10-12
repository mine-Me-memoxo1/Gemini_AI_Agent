import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = None
if len(sys.argv) == 1:
    raise Exception('No prompt given')
else:
    user_prompt = sys.argv[1]
   
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
response = client.models.generate_content(model='gemini-2.0-flash-001', contents = messages)

print(response.text)
if '--verbose' in sys.argv[2:]:
    print('User prompt: {}'.format(user_prompt))
    print('Prompt tokens: {}'.format(response.usage_metadata.prompt_token_count))
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
