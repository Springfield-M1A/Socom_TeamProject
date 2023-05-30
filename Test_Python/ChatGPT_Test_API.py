# Python >= 3.8 installed
# Use VSCode
# pip install openai

# search URL https://platform.openai.com/ and LOGIN, and generate API Keys

import openai

openai.api_key = ""
# Copy your API Keys in ""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    massages=[
        {
            "role": "user",
            "content": "Hi? Can you hear me?",
        }
    ],
)
print(completion)
