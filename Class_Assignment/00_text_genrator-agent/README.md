# Writer Agent using Gemini 1.5 Flash
This is a simple yet powerful Python-based Writer Agent that uses **Google's Gemini 1.5 Flash** model to generate creative text like poems, stories, essays, and emails. The project is designed to demonstrate how AI can be used to assist in writing tasks using a custom agent-based structure.

---
## Features

- 🤖 Agent-based architecture
- 🧠 Uses `Gemini 1.5 Flash` (Google Generative AI)
- 📝 Creative content generation (poems, stories, essays)
- 🔒 Secure API key usage with `.env` file
- ⚙️ Easy to extend for other roles (e.g., Translator, Coder)

---
##  Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/writer-agent-gemini.git
cd writer-agent-gemini
```

### 2. Create & activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Set your API key

Create a .env file in the root directory and add your API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```
You can get your API key from Google AI Studio.

## How to Run
```bash
python main.py
```

## Project Structure

```
.
├── main.py              # Main script to run the Writer Agent
├── .env                 # Stores your API key (excluded from version control)
└── README.md            # Project documentation
```
## How It Works
The agent is built using a simple Python class that:

- Accepts a role-based instruction (e.g., "You are a writer agent...")

- Passes user input and instructions to the Gemini model.

- Returns a human-readable response.

```python
model = genai.GenerativeModel("models/gemini-1.5-flash")
response = model.generate_content(full_prompt)
```
## Example Output
```bash
Pale orb in velvet skies so deep,  
A silent watch while mortals sleep.  
A silver sickle, then a gleam,  
Reflecting sun, a whispered dream...
```
##  Extendability
You can easily create more agents with different roles, such as:

- CoderAgent — for code generation

- TranslatorAgent — for multilingual text

- EditorAgent — for rewriting/improving text

Just change the instruction string and prompt style!

##  License
This project is open-source and available for educational and personal use.

## Contributing
Pull requests and suggestions are welcome. Let’s build smarter agents together!

## Credits

Built with  by Syeda Qurrat using Google Generative AI SDK.