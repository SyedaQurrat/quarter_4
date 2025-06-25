# custom_agents/agent_a.py

# from agents import Agent, ChatMessage
from tools.crypto_tool import get_crypto_rate
from custom_agents.agent_b import agent_b
from openai_agents import Agent, ChatMessage

agent_a = Agent(
    name="Agent A",
    process=lambda input, _: f"Agent A ne kaha: {input}"
)
@agent_a.on_message
async def handle_a(message: ChatMessage):
    if "crypto" in message.content.lower():
        return await agent_a.handoff(agent_b, message)
    return "I'm AgentA. No crypto mentioned, so I am responding directly."
