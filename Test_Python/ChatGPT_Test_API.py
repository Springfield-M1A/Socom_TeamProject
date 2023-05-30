# Python >= 3.8 installed
# Use VSCode
# pip install openai

# search URL https://platform.openai.com/ and LOGIN, and generate API Keys
"""Base model code
import os
import openai

openai.api_key = "OPENAI_API_KEY"
# Copy your API Keys instend OPENAI_API_KEY

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    massages = [
        {
            "role": "user",
            "content": "Hi? Can you hear me?",
        }
    ],
)
print(completion.choices[0].message)
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []
while True:
    completion = openai.ChatCompletion.create(model = "gpt-3.5-tubo", messages = messages)

    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")
    