# run.py

from agents import Runner
from config import config
from custom_agents.agent_a import agent_a

runner = Runner(config=config, agents=[agent_a])
