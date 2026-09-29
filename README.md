# Travel Helper Agent

An AI-powered travel assistant built with **Python, Groq, OpenAI-compatible tool calling, Tavily, Open-Meteo, and Gradio**.

The agent can research destinations, retrieve information from a local travel knowledge base, check current weather, remember previous conversation context, and return validated structured responses using **Pydantic**.

---

## Overview

Travel Helper is an agentic AI application designed to demonstrate practical **LLM tool calling and agent workflows**.

Instead of relying only on the model's internal knowledge, the agent can dynamically decide when external tools are required.

### The agent can:

* Research travel destinations using web search
* Retrieve information from local travel documents
* Get current weather information
* Handle multi-tool requests
* Maintain conversation context across turns
* Handle tool failures and missing information
* Generate structured responses
* Validate final responses with Pydantic
* Provide observable tool-call logs for debugging
* Run through a clean Gradio chat interface

---

## Architecture

```text
                         ┌──────────────────────┐
                         │        User          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Gradio UI        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Travel Agent      │
                         │      main.py        │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │   Groq LLM           │
                         │ gpt-oss-120b         │
                         └──────────┬───────────┘
                                    │
                         Tool decision / calling
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
     ┌──────────────┐      ┌─────────────────┐     ┌───────────────┐
     │  Web Search  │      │ Local Retrieval │     │    Weather    │
     │    Tavily    │      │   TXT files     │     │  Open-Meteo   │
     └──────────────┘      └─────────────────┘     └───────────────┘
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Tool Results         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Structured Response  │
                         │      Pydantic        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Final Answer         │
                         └──────────────────────┘
```

---

## Features

### 1. Web Search

The agent can search the web when current or external travel information is required.

Powered by:

* Tavily Search API
* Configurable search depth
* Multiple search results
* Source URLs included in the tool output

Example:

```text
What are the best attractions to visit in Tokyo?
```

The agent can decide to call:

```text
search_web
```

---

### 2. Local Travel Knowledge Base

The project includes a lightweight retrieval system over local `.txt` documents.

The current implementation uses keyword-based retrieval rather than a vector database, keeping the project lightweight and easy to understand.

Example:

```text
What transportation options are available in Tokyo?
```

The agent can call:

```text
retrieve_travel_documents
```

The tool searches the local:

```text
data/
```

directory and ranks matching documents based on keyword overlap.

---

### 3. Current Weather

The agent can retrieve current weather conditions using the **Open-Meteo API**.

The weather tool accepts:

```json
{
  "latitude": 35.6762,
  "longitude": 139.6503
}
```

and returns information such as:

* Temperature
* Weather code
* Wind speed

Example:

```text
What's the current weather in Tokyo?
```

The agent can use:

```text
get_weather
```

---

## Agentic Workflow

The project uses a tool-calling loop.

```text
User Question
      │
      ▼
LLM decides
      │
      ├── No tool required
      │       │
      │       ▼
      │   Final response
      │
      └── Tool required
              │
              ▼
         Tool execution
              │
              ▼
         Tool result
              │
              ▼
        LLM continues
              │
              ▼
        Final response
```

The loop supports up to 10 agent steps to prevent uncontrolled execution.

---

## Memory

Conversation history is passed back to the model on every turn.

For example:

```text
User:
I'm planning a 7-day trip to Japan.

Assistant:
...

User:
What about Kyoto?
```

The second question can be interpreted using the previous conversation context.

The agent can therefore retain information such as:

* Destination
* Travel dates
* Number of travelers
* Trip duration
* Budget
* Interests
* Previous travel decisions

No separate database is required for the basic conversational memory implementation.

---

## Structured Output

The final response is represented using a Pydantic model:

```python
class TravelResponse(BaseModel):
    answer: str
    tools_used: list[str]
    sources: list[str]
    confidence: float
```

Example:

```json
{
  "answer": "Tokyo is a great destination...",
  "tools_used": [
    "search_web"
  ],
  "sources": [
    "https://example.com"
  ],
  "confidence": 0.92
}
```

This provides a predictable response contract instead of relying on unstructured LLM text.

---

## Tool Calling

The project exposes three tools to the model.

### `search_web`

Searches the web for travel-related information.

```python
search_web(query: str)
```

### `retrieve_travel_documents`

Searches the local travel knowledge base.

```python
retrieve_travel_documents(query: str)
```

### `get_weather`

Retrieves current weather information.

```python
get_weather(latitude: float, longitude: float)
```

The LLM chooses the appropriate tool based on the user's request.

---

## Error Handling

The tools include basic error handling.

Examples include:

```text
ERROR: Search query cannot be empty.
```

```text
No web results found for: ...
```

```text
No relevant travel information found for: ...
```

```text
Weather request failed: ...
```

The agent is instructed not to fabricate information when a tool fails.

When evidence is incomplete, the final response can reduce its confidence score.

---

## Project Structure

```text
Travel-Helper-Agent/
│
├── data/
│   ├── destinations.txt
│   ├── transportation.txt
│   ├── travel_tips.txt
│   └── ...
│
├── context.py
├── tools.py
├── main.py
├── styles.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `main.py`

Contains:

* Groq/OpenAI-compatible client
* Agent loop
* Conversation history
* Structured output generation
* Pydantic validation
* Gradio application

### `tools.py`

Contains:

* Tool implementations
* Tool schemas
* Tool mapping
* Tool execution handler

### `context.py`

Contains the Travel Helper system prompt and agent behavior rules.

### `styles.py`

Contains:

* UI theme
* CSS
* JavaScript
* Example prompts

### `data/`

Contains the local travel knowledge base used by the retrieval tool.

---

## Tech Stack

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Core development             |
| Groq          | LLM inference                |
| `openai`      | OpenAI-compatible API client |
| Tavily        | Web search                   |
| Open-Meteo    | Weather API                  |
| Pydantic      | Structured output validation |
| Gradio        | Web interface                |
| Requests      | HTTP API requests            |
| python-dotenv | Environment variables        |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Travel-Helper-Agent.git
cd Travel-Helper-Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

DEFAULT_MODEL_NAME=openai/gpt-oss-120b
```

Never commit your `.env` file.

Add it to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## Running the Application

Start the Gradio application:

```bash
python main.py
```

The terminal should display a local Gradio URL.

Open the URL in your browser and start chatting with the Travel Helper.

---

## Example Queries

### No Tool Required

```text
What can you help me with?
```

The agent should answer directly without calling a tool.

---

### Web Search

```text
What are the best attractions to visit in Tokyo?
```

Expected tool:

```text
search_web
```

---

### Local Retrieval

```text
What does the local travel guide say about transportation?
```

Expected tool:

```text
retrieve_travel_documents
```

---

### Weather

```text
What is the current weather in Tokyo?
```

Expected tool:

```text
get_weather
```

---

### Multi-Tool Request

```text
I'm planning a trip to Tokyo. What should I visit,
what does my travel guide recommend, and what's the
current weather?
```

The agent may use multiple tools depending on the available information.

---

### Memory / Follow-up

First:

```text
I'm planning a 7-day trip to Japan.
```

Then:

```text
What about Kyoto?
```

The second question should use the previous conversation context.

---

### Tool Failure

```text
Search for:
```

This should trigger validation in the web-search tool because the query is empty.

Another example:

```text
Tell me about a completely fictional destination called
XYZ-UNKNOWN-123456.
```

The search/retrieval system may return no relevant results.

---

## Debugging and Verbose Agent Trace

The application prints agent activity in the terminal.

Example:

```text
============================================================
Agent step: 1
============================================================

Finish reason: tool_calls

Tool calls detected: 1

Tool called: search_web
Arguments: {'query': 'best attractions in Tokyo'}
```

After the tool result is returned, the LLM receives the result and can continue the agent loop.

The terminal also prints the final structured response:

```text
============================================================
FINAL STRUCTURED RESPONSE
============================================================

{
  "answer": "...",
  "tools_used": [
    "search_web"
  ],
  "sources": [
    "https://..."
  ],
  "confidence": 0.91
}
```

This makes the agent behavior observable during development.

---

## V1 → V2 Improvements

The project can be developed incrementally.

### V1

The initial version focuses on:

* Basic tool calling
* Three travel tools
* Conversation history
* Simple local retrieval
* Basic error handling

### V2

The improved version adds:

* Better tool descriptions
* More explicit tool schemas
* Stronger tool-selection instructions
* Tool failure handling
* Source tracking
* Structured Pydantic output
* Confidence estimation
* Separation between tool execution and final response generation

This separation is especially important because the final structured-output request does **not** receive the tool definitions. This prevents the model from confusing the response schema with an executable tool.

---

## Design Principles

The project follows several practical agent-development principles:

### 1. Tool Calling Over Hallucination

When reliable external information is required, the agent should use the appropriate tool rather than guessing.

### 2. Explicit Tool Contracts

Every tool exposes a clear name, description, and JSON schema.

### 3. Observable Execution

Tool calls and arguments are logged during development.

### 4. Structured Responses

The final response is validated using Pydantic.

### 5. Graceful Failure

Failed tools should produce explicit errors rather than fabricated information.

### 6. Conversational Context

Previous user messages are included in subsequent turns to support follow-up questions.

---

## Future Improvements

Possible next steps include:

* Replace keyword retrieval with embeddings
* Add a vector database such as Qdrant or Chroma
* Add destination geocoding
* Automatically resolve city names into coordinates
* Add hotel and flight search
* Add itinerary generation
* Add budget estimation
* Add map integration
* Add persistent memory
* Add evaluation datasets
* Add automated agent tests
* Add tool retry policies
* Add observability and tracing
* Add streaming responses
* Deploy the application to Hugging Face Spaces

---

## Learning Objectives

This project demonstrates practical concepts in modern AI agent development:

* LLM tool calling
* Function calling
* Agent loops
* Multi-tool orchestration
* API integration
* Retrieval-augmented workflows
* Conversational memory
* Structured generation
* Pydantic validation
* Error handling
* Agent observability
* Gradio application development

---

## Author

**Ahmed Taha**

AI Engineer focused on:

* LLM Applications
* RAG Systems
* AI Agents
* LangChain / LangGraph
* AI API Integration
* Production-oriented AI Systems

---

## Disclaimer

Travel information can change over time. The agent should use external tools for information that requires current verification, and users should independently verify important travel details before making bookings or travel decisions.
