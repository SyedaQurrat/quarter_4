# custom_agents/agent_b.py

from agents import Agent, ChatMessage, tool_call
from tools.crypto_tool import get_crypto_rate

agent_b = Agent(
    name="AgentB",
    system_message="You are a crypto agent. Use tools to get crypto rates.",
    tools=[get_crypto_rate],
)

@agent_b.on_message
async def handle_b(message: ChatMessage):
    return await tool_call(get_crypto_rate, symbol="BTC")
