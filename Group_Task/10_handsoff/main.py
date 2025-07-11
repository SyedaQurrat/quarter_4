import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("API_KEY is not set. Please chechk your .env file!")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

lyric_agent = Agent(
    name="LyricAnalyzer",
    instructions="You analyze lyric poetry. If poem contains emotions or feelings, describe it with explanation.",
    model=model
)

narrative_agent = Agent(
    name="NarrativeAnalyzer",
    instructions="You analyze narrative poetry. If poem tells a story, describe the plot and structure.",
    model=model
)

dramatic_agent = Agent(
    name="DramaticAnalyzer",
    instructions="You analyze dramatic poetry. If poem is meant to be performed, explain its monologue/dialogue form.",
    model=model
)

triage_agent = Agent(
    name="PoetryTriageAgent",
    instructions="""You are a triage agent. Decide the type of poetry (lyric, narrative, dramatic) and forward the task to the correct analyzer agent.""",
    handoffs=[lyric_agent, narrative_agent, dramatic_agent],
    model=model
)

poem_input = """
I walk alone under the sky so wide,  
Thinking of you, with tears I hide.  
Memories echo like waves at sea,  
Your love still lingers inside of me.
"""

# LLM decides agent handoff automatically!
result = Runner.run_sync(triage_agent, poem_input, run_config=RunConfig)

print("\nDramaticAnalyzer:\n")
print(result.final_output)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)