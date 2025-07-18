#  Basic setup and imports
import os
from dotenv import load_dotenv
import chainlit as cl
# from openai import AsyncOpenAI

from agents import AsyncOpenAI, OpenAIChatCompletionsModel

#  Load environment variables from .env
load_dotenv()
 #  Get GEMINI_API_KEY from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

#  Error if API key not found
if not gemini_api_key:
    raise ValueError(" GEMINI_API_KEY not set in .env file!")

#  Setup Gemini API using OpenAI-style client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# Gemini Flash model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
    
)

#  This function runs when user sends a message
@cl.on_message
async def on_message(msg: cl.Message):
    #  Prepare message in OpenAI-style format
    messages = [
        {"role": "user", "content": msg.content}
    ]

    #  Send to Gemini Flash
    res = await client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=messages
    )

    #  Respond to user in Chainlit
    await cl.Message(content=res.choices[0].message.content).send()

#  Optional: Welcome message on chat start
@cl.on_chat_start
async def start():
    await cl.Message(content=" Gemini Flash ready to chat!").send()
