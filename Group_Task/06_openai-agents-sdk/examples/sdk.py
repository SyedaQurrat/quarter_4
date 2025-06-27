# sdk.py
from context import Agent
from runner import AgentRunner

agent = Agent(name="SimpleAgent", instructions="Just echo the message back.")
runner = AgentRunner(agents=[agent])

print(" AgentRunner started!\n")

# Example run without loop
user_input = "Hello from Syeda!"
response = runner.run(user_input)
print("Response:", response)
