# from agents import Agent

# writer = Agent(
#     name = 'writer Agent',
#     instructions= 'you are a writer Agent. Generate Poem, Stories, Essay and Email etc.'
# )



import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Custom Agent class
class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def run(self, prompt):
        # Correct model name used here
        model = genai.GenerativeModel("gemini-1.5-flash")
        full_prompt = f"{self.instructions}\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text

# Create writer agent
writer = Agent(
    name="Writer Agent",
    instructions="You are a writer agent. Generate creative content like poems, stories, essays, and emails."
)

# Run agent
output = writer.run("Write a short poem about the moon.")
print(output)
