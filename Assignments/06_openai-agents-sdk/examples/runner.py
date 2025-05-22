# runner.py
from context import Agent

class AgentRunner:
    def __init__(self, agents):
        self.agents = agents

    def run(self, input):
        agent = self.agents[0]
        return f"{agent.name} (responding to): {input}"
