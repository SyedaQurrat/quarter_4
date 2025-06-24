# import chainlit as cl
# import openai
# from monkey_patch_gemini import *

# @cl.on_chat_start
# async def start():
#     await cl.Message(content="👋 Hi! I’m your Gemini-powered chatbot. How can I help you today?").send()

# @cl.on_message
# async def handle_message(message: cl.Message):
#     prompt = message.content

#     response = openai.ChatCompletion.create(
#         model="gemini-1.5-flash",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )

#     reply = response["choices"][0]["message"]["content"]
#     await cl.Message(content=reply).send()





# app.py

import chainlit as cl
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Translation Agent
@cl.on_message
async def translate_agent(message: cl.Message):
    try:
        # Message should be in format: "Translate from Urdu to English: Mujhe bhook lagi hai"
        user_prompt = message.content.strip()

        # Gemini ko prompt bhejna
        full_prompt = f"""
        You are a translation agent. Translate the following sentence into the target language as asked.
        
        Sentence and instruction:
        {user_prompt}
        
        Just give the translated sentence, no explanation.
        """

        # Gemini se response lena
        response = model.generate_content(full_prompt)

        # Output user ko bhejna
        await cl.Message(content=response.text.strip()).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
