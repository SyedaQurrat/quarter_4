# main.py

import chainlit as cl
from run import runner

@cl.on_chat_start
async def start():
    cl.user_session.set("runner", runner)

@cl.on_message
async def handle_msg(message: cl.Message):
    runner = cl.user_session.get("runner")
    response = await runner.run(message.content)
    await cl.Message(content=response).send()
