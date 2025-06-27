# from openai import AsyncOpenAI
# from openai.types.beta.threads import Message
# from openai.agents import Agent, Runner
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro"
# )

# # 🔁 Translator Agent
# translator_agent = Agent(
#     name="Translator",
#     instructions="You are an expert English to Urdu translator. Always reply only in Urdu.",
#     model="gemini-pro"
# )

# # 📄 Summarizer Agent
# summarizer_agent = Agent(
#     name="Summarizer",
#     instructions="You are an expert at summarizing text in simple English.",
#     model="gemini-pro"
# )

# # 🤖 Runner to manage agent flow
# runner = Runner(
#     agents=[translator_agent, summarizer_agent],
#     client=client
# )

# # 🌐 Chainlit will use this entry point
# async def main():
#     user_input = "Please translate: 'Knowledge is power'. Then summarize this: 'Artificial Intelligence is changing the world by automating tasks and enhancing decision-making.'"
#     response = await runner.run(user_input)
#     print(response)




from openai import AsyncOpenAI
# from openai.types.beta.threads import Message
# from openai.types.beta.tools import ToolCall
from openai.agents import Agent, RunnableAgent, run_agent
from openai.types.shared_params import FunctionDefinition
from openai_agent_sdk.models.openai_model import OpenAIChatCompletionsModel
from openai_agent_sdk.runner.run_config import RunConfig
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Urdu Translator",
    instructions="Translate English to Urdu. Only reply in Urdu.",
    model=model
)

async def main():
    input = "Translate this: The future of AI is very exciting."
    result = await run_agent(agent, input, config=config)
    print(result)
