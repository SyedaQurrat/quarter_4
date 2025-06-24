
# function-vs-tool-calling

# Function Calling vs Tool Calling in Python and AI Agents

This guide covers both **Function Calling** (basic to advanced Python) and **Tool Calling** (used in AI agent systems like OpenAI SDK). It explains the definitions, use cases, when to use, benefits, drawbacks, and provides code examples with line-by-line explanation.

---

##  Part 1: Function Calling (Python)

### Definition:
> Function calling means invoking a block of reusable code that performs a specific task.

---

###  Why We Use:
- Code reusability
- Modular structure
- Avoid repetition
- Easy to test & maintain

---

###  Basic Syntax:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Syeda")

```

### Line-by-line Explanation:
- def greet(name): → defines a function with a parameter name.

- print(...) → displays the greeting message.

- greet("Syeda") → calls the function with "Syeda" as the argument.



 ### When to Use:
- Repetitive tasks

- Clean, readable code

- Shared logic between components

## When Not to Use:
- Tiny one-liners (could use lambdas)

- Over-abstraction leading to confusion

- Poorly named or non-descriptive functions

### Advanced Concepts:
- **return** values

- Default parameters

- *args / **kwargs

- Recursive functions

- Lambda expressions

- Higher-order functions

## 🔹 Part 2: Tool Calling (AI Agents)

### ✅ Definition

**Tool calling** is the ability of an AI model (like OpenAI GPT) to **invoke external tools** — such as Python functions, APIs, or external services — **automatically** in response to user queries.

This allows the model to go beyond just generating text and actually perform real-world actions.

---

### 🔧 Why We Use Tool Calling

- ✅ Extend LLM functionality
- ✅ Fetch live data (e.g., weather, crypto prices, user info)
- ✅ Perform real-world tasks (e.g., send emails, trigger APIs)
- ✅ Enable structured automation and decision making

---

### 🧠 When to Use Tool Calling

- 🔹 When tasks require **external information** that LLM doesn’t know
- 🔹 When your app needs to **execute backend logic**
- 🔹 When the user prompt cannot be solved by text generation alone

---

### ❌ Misuse or Pitfalls

- ❌ Tool functions lack **proper input validation**
- ❌ Tool calls made **unnecessarily or redundantly**
- ❌ **Wrong tool** triggered due to poor intent classification

---

## 🧪 Tool Calling Example using OpenAI SDK

Here’s how to implement a simple tool that fetches weather based on a city using OpenAI SDK:

```python
from openai import OpenAI
from openai.types import ToolFunction
from pydantic import BaseModel
```

# Step 1: Define the input model using Pydantic
class WeatherInput(BaseModel):
    city: str

# Step 2: Create the actual function that will be called
``` def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny and 30°C."
```
# Step 3: Wrap the function as a ToolFunction for the agent
``` weather_tool = ToolFunction(
    name="get_weather",
    description="Get weather info of a city",
    func=get_weather,
    input_schema=WeatherInput
)
```

# Step 4: Set up the OpenAI client and call the tool
``` client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Karachi?"}],
    tools=[weather_tool],
    tool_choice="auto"
)
```
# 1. Define input model
```class WeatherInput(BaseModel):
    city: str
```
# 2. Tool function
``` def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny and 30°C."
```
# 3. Wrap in ToolFunction
``` weather_tool = ToolFunction(
    name="get_weather",
    description="Get weather info of a city",
    func=get_weather,
    input_schema=WeatherInput
)
```
# 4. Call through OpenAI SDK
```client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Karachi?"}],
    tools=[weather_tool],
    tool_choice="auto"
)
```
## 🔍 Line-by-line:
BaseModel defines input schema (city).

get_weather() performs the actual logic.

ToolFunction wraps the Python function.

client.chat.completions.create() executes it based on the user prompt.

## 🔄 Function vs Tool Calling – Comparison
Feature	Function Calling	Tool Calling (AI SDKs)
Usage	Normal Python apps	AI Agents & Language Models
Triggered By	Developer manually	LLM automatically (via tool_choice)
Input	Arguments	Validated models (e.g., Pydantic)
Purpose	Logic building & reuse	Extend LLM capabilities
Real Use	Internal code	External services or data access

## ✅ Summary
Use Function Calling in regular apps for logic reuse.

Use Tool Calling in AI systems when you want the model to perform real-world tasks.

Validate tool input and avoid overcomplicating logic.

## 📚 Reference:
OpenAI Tool Calling Documentation:
https://platform.openai.com/docs/assistants/tools/function-calling

