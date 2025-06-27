# OpenAI Agents SDK Overview
This README provides a structured explanation and answers to key questions about the **OpenAI Agents SDK**, focusing on core components like `Agent`, `Runner`, `TContext`, and Python concepts like `dataclass` and `generics`.

## What is SDK?
SDK stands for **Software Development Kit**. It is a set of tools, libraries, and documentation that helps developers build applications for a specific platform or framework. It includes pre-built functions, APIs, and guidelines that make development easier and faster. For example, an SDK helps you write code without building everything from scratch.

## What Does the OpenAI Agents SDK Do?
The OpenAI Agents SDK is a toolkit that assists developers in creating AI-based applications, particularly AI agents that can work autonomously (agentic AI apps). It is an upgraded version of OpenAI's earlier Swarm framework and works with Python. Its primary purpose is to provide developers with an easy way to build AI agents and manage their workflows. It is production-ready and designed for real-world applications.

### Main Features and Functions
- **Building Agents**: It configures large language models (LLMs) as agents. Each agent has specific instructions and tools to perform tasks like web search or data processing.
- **Handoffs**: This feature allows one agent to delegate its work to another agent. For instance, if a task is beyond an agent’s scope, it can pass the task to a specialized agent.
- **Guardrails**: These are for safety checks. They validate inputs and outputs to ensure the agent doesn’t provide incorrect or harmful responses, ensuring responsible AI behavior.
- **Tracing and Debugging**: It includes built-in tracing to help developers visualize and debug agent workflows. You can see what the agent is doing, which tools it’s using, and where issues might be occurring.
- **Tools Integration**: You can convert any Python function into a tool. These tools help agents perform external tasks like web searches, file retrieval, or API calls.
- **Multi-Agent Workflows**: It is designed to coordinate multiple agents. This means you can have different agents working together on complex tasks.

### Example Use Case
Suppose you want to build a banking system where AI agents handle customer queries:
- A **Customer Service Agent** listens to the customer’s question.
- If the question is about a loan, it hands off the task to a **Loan Specialist Agent**.
- Guardrails ensure the inputs are safe and responses are in the correct format.
- Through tracing, you can see which agent is doing what.

### How to Use It?
1. Set up a Python environment.
2. Install the OpenAI Agents SDK (`pip install openai-agents`).
3. Set your OpenAI API key.
4. Write code to define agents, set their tools and handoffs, and run workflows.

This SDK is built for developers who want to create autonomous AI systems that can think and work independently, such as for research automation, customer support, or enterprise workflows. Its focus is on both simplicity and power, so you can easily build complex applications.

# Understanding Runner and Context in OpenAI Agents SDK

## What is a Runner?
A Runner is a core component in the OpenAI Agents SDK that executes and manages the workflows of one or more agents. It acts like an engine that runs the agents' tasks, handles their interactions, and ensures everything operates correctly.

### Purpose
- The Runner processes the agent’s instructions, tools, and handoffs. It decides which agent should work, when, and how.

### Example
If you have a customer support agent processing a query, the Runner activates that agent, calls its tools (e.g., database access), and, if needed, hands off the task to another agent.

### Implementation
In code, you use the `AgentRunner` class. It takes your agents and their configurations and runs them.

## What is Context?
Context is a data structure or environment that holds the current state of an agent and the necessary information for its tasks. It informs the agent about what has happened so far and what needs to be done next.

### Purpose
- Context contains messages, memory, and state-related data used for the agent’s decision-making. It acts as a shared memory that updates during the agent’s interactions.

### Example
If a customer support agent is interacting with a user, the context stores the user’s previous messages, the agent’s responses, and relevant data (like the user’s account number). This helps the agent remember the conversation flow.

### Implementation
In the OpenAI Agents SDK, context is automatically managed when you run agents through the Runner. You can also manually update the context if needed.

## Relationship Between Runner and Context
- The Runner uses the context to provide agents with the right information and track their tasks.
- Context serves as a foundation for the Runner, helping it understand what the agent needs to do and its current state.

## Simple Code Example
```python
from openai_agents import Agent, AgentRunner

# Create an agent
agent = Agent(name="SupportAgent", instructions="Answer customer queries")

# Create a runner
runner = AgentRunner(agents=[agent])

# Run with context (context is automatically managed)
response = runner.run(input="What is my account balance?")
print(response)
```

# OpenAI Agents SDK: Key Concepts Explained

## 1. Why is the Agent Class Defined as a Dataclass?
A dataclass is a Python feature that simplifies class creation when you need to store data. The Agent class is defined as a dataclass because it primarily needs to store data such as the agent's name, instructions, and tools. A dataclass automatically generates boilerplate code (like `__init__` and `__repr__`), making the code shorter, cleaner, and more readable. Since the Agent class’s main role is to hold the agent’s configuration, a dataclass is an ideal choice.

## 2a. Why is the System Prompt Stored as Instructions in the Agent Class? And Why Can It Also Be Set as a Callable?
The system prompt (referred to as instructions) is stored in the Agent class because it defines the core behavior of the agent—it specifies how the agent should function. The instructions can be a fixed string that describes the agent’s role, such as "Answer customer queries." However, it can also be set as a callable (a function) because sometimes the instructions need to be dynamic—meaning they must change based on the context or input. For example, you might use a function that generates instructions based on the user’s input. This design provides flexibility.

## 2b. Why is the User Prompt Passed as a Parameter in the Runner’s Run Method, and Why is This Method a Classmethod?
The user prompt is passed as a parameter in the Runner’s `run` method because it is the user’s input at runtime, which can vary with each query. While the agent’s instructions are fixed (or dynamically set via a callable), the user prompt changes with every query, so it needs to be passed at runtime. The `run` method is a classmethod because the Runner class acts like a factory or manager—it can run agents without needing to create an instance of the Runner. Using a classmethod makes the code more modular and reusable.

## 3. What is the Purpose of the Runner Class?
The purpose of the Runner class is to manage and execute the workflows of agents. It acts as a controller that activates agents, runs their tasks, handles handoffs (transferring tasks from one agent to another), and tracks the context. Essentially, it ensures that all agents work correctly and their coordination is seamless. For example, if one agent needs help from another agent, the Runner manages that handoff.

## 4. What Are Generics in Python? Why Do We Use Them for TContext?
Generics in Python are used for typing when you need to make a class or function flexible while maintaining type safety. They allow you to define a type variable (e.g., `T`) that can later be replaced with a specific type (e.g., `str`, `int`). We use generics for `TContext` because the type of context can vary across different projects. For instance, in one project, the context might be a dictionary, while in another, it might be a custom object. Using generics (like `TContext`) makes the code more flexible and reusable, and type checking helps reduce errors. This gives developers the freedom to define the context type according to their needs.

## Conclusion

This document provides a detailed overview of the OpenAI Agents SDK, explaining its purpose, features, and key concepts like the Agent class, Runner class, and context. It also covers advanced topics like generics in Python and their use in the SDK. The code example demonstrates how to implement a basic agent workflow. This SDK is a powerful tool for developers looking to build autonomous AI systems for real-world applications like customer support or research automation

## References

The information in this document was gathered from the following sources:

- [OpenAI Official Website](https://openai.com/) - For general information about OpenAI and its projects.
- [OpenAI API Documentation](https://platform.openai.com/docs/) - For understanding OpenAI's API and related tools.
- [Python Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html) - For details on Python dataclasses used in the Agent class.
- [Python Typing and Generics](https://docs.python.org/3/library/typing.html) - For understanding generics in Python.
- [Swarm Framework by OpenAI](https://github.com/openai/swarm) - Since OpenAI Agents SDK is an upgraded version of Swarm, this provided context on multi-agent systems.

## Acknowledgments


I would like to thank my teacher for assigning this research task, which helped me learn about AI agents and SDKs. Additionally, I appreciate the resources provided by OpenAI and the Python community for their detailed documentation.


