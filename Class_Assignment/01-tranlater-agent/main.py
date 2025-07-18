import os
from dotenv import load_dotenv
import chainlit as cl
from agents import AsyncOpenAI

#  Load API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

#  Setup Gemini client (OpenAI style)
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#  Translator Agent class (like WriterAgent)
class TranslatorAgent:
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

# Create the Translator Agent
translator_agent = TranslatorAgent(
    name="Translator Agent",
    instructions="""
You are a professional translator. 
When a user asks like: 'Translate to Urdu: The future is bright.',
you must detect the target language and return only the translated sentence.
Do not include explanation, just output the translation.
"""
)

# Handle user messages
@cl.on_message
async def on_message(msg: cl.Message):
    user_input = msg.content
    response = await translator_agent.run(user_input)
    await cl.Message(content=response).send()

# 🙋 Optional welcome
@cl.on_chat_start
async def start():
    await cl.Message(
        content="Translator Agent is ready!\nSend: `Translate to Urdu: The world is changing fast.`"
    ).send()
