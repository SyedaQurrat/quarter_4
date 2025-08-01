import os
from dotenv import load_dotenv
import chainlit as cl

#from openai import
from agents import AsyncOpenAI

#  Load API Key from .env file
load_dotenv()
# Get GEMINI_API_KEY from enviroment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Error if API key is not found
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# 🔧 Setup Gemini client using OpenAI-style SDK
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#  Writer Agent Class
class WriterAgent:
    def __init__(self, name, instructions, model_name="gemini-2.0-flash"):
        self.name = name
        self.instructions = instructions
        self.model_name = model_name

    async def run(self, user_prompt):
        messages = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": user_prompt}
        ]
        res = await client.chat.completions.create(
            model=self.model_name,
            messages=messages
        )
        return res.choices[0].message.content

#  Create the Writer Agent
writer_agent = WriterAgent(
    name="Writer Agent",
    instructions="You are a creative writing agent. Generate beautiful poems, stories, essays, and emails."
)

#  Chainlit: Handle user messages
@cl.on_message
async def on_message(msg: cl.Message):
    user_input = msg.content
    response = await writer_agent.run(user_input)
    await cl.Message(content=response).send()

#  Optional: Welcome message
@cl.on_chat_start
async def start():
    await cl.Message(content=" Writer Agent is read! Send me a topic and I’ll write for you ").send()
    