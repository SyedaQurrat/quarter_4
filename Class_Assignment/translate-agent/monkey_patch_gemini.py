# import google.generativeai as genai
# import os

# # Gemini API key environment variable se lo
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")

# def fake_gemini_response(prompt):
#     response = model.generate_content(prompt)
#     return response.text

# file: monkey_patch_gemini.py

import openai
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define a fake ChatCompletion that mimics OpenAI but uses Gemini
class GeminiChat:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.chat = self.model.start_chat()

    def create(self, model, messages, **kwargs):
        user_prompt = "\n".join([msg["content"] for msg in messages if msg["role"] == "user"])
        response = self.chat.send_message(user_prompt)
        return {"choices": [{"message": {"content": response.text}}]}

# Monkey patch OpenAI SDK to use Gemini
openai.ChatCompletion = GeminiChat()
